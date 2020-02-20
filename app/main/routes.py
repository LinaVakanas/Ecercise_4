from flask import render_template, Blueprint, url_for, flash, redirect, request
from sqlalchemy.exc import IntegrityError

from app import db
from app.main.forms import SignupForm, CityBlogSearchForm
from app.models3 import User, City, Forecast

bp_main = Blueprint('main', __name__)


@bp_main.route('/signup/', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    search = CityBlogSearchForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, name=form.name.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Exciting, you have successfully signed up!')
            return redirect(url_for('main.home',  title='Home', search=search))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Sorry we were unable to register you. '
                  'Please check your details are correct and try again')
    return render_template('signup.html', form=form, title="Signup")


@bp_main.route('/', methods=['GET', 'POST'])
def home():
    search = CityBlogSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    else:
        return render_template('index.html', search=search, title="Home")
#
#
@bp_main.route('/results/', methods=['POST', 'GET'])
def search_results(search):
    results = []
    search_string = search.search.data.lower()
    select_string = search.select.data
    if search_string == '':
        flash("Enter a city or blog...")
        return redirect('/')

    if select_string == 'City':
        results = Forecast.query.join(City).filter(City.city.contains(search_string)).all()
        if not results:
            flash('Hm... looks like we have nothing on {searched}!'.format(searched=search_string.capitalize()))
            return redirect('/')
        else:
            return render_template('search_results_city.html', title='Search Results', results=results, searched=search_string)

    if select_string == 'Blog':
        results = Forecast.query.join(City).filter(Forecast.forecast.contains(search_string)).all()
        if not results:
            flash("Hm... we don't know '{searched}', looks like you made up that blog!".format(searched=search_string))
            return redirect('/')
    return render_template('search_results_blogs.html', title='Search Results', results=results, searched=search_string)


@bp_main.route('/posts/', methods=['GET'])
def view_posts():
    blogs = Forecast.query.join(City).join(User).\
        with_entities(Forecast.forecast, User.username, User.name.label('author'), City.city).all()
    return render_template('posts.html', title='Posts', posts=blogs)


@bp_main.route('/bloggers', methods=['GET'])
def view_bloggers():
    blogger = User.query.all()
    return render_template('bloggers.html', title='Bloggers', bloggers=blogger)

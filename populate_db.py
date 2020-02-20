from app import db
from app.models3 import User, City, Forecast

def populate_db():

    if not User.query.first():
        u1 = User(user_id=1, username='weatherman', email='jo@bloggs.com')
        u2 = User(user_id=2, username='itrains', email='itrains@alot.co.uk')
        u3 = User(user_id=3, username='sunny', email='sunny_grl@sunshine.co.uk')

        c1 = City(city_id=1, city='London')
        c2 = City(city_id=2, city='Manchester')
        c3 = City(city_id=3, city='Birmingham')
        c4 = City(city_id=4, city='Edinburgh')
        c5 = City(city_id=5, city='Belfast')
        c6 = City(city_id=6, city='Cardiff')

        p1 = Forecast(id=1, city_id=2, user_id=2, forecast_datetime='2020-01-27 9:00:00', forecast='Moderate rain', comment='It is really likely to rain today, sorry folks')
        p2 = Forecast(id=2, city_id=6, user_id=1, forecast_datetime='2020-01-27 9:00:00', forecast='Heavy rain', comment="Don't leave home without full waterproofs today!")
        p3= Forecast(id=3, city_id=1, user_id=3, forecast_datetime='2020-01-27 9:00:00', forecast='No rain', comment='No umbrella required.')

        db.session.add_all([c1, c2, c3, c4, c5, c6])
        db.session.add_all([u1, u2, u3])
        db.session.add_all([p1, p2, p3])
        db.session.commit()
from app import db


class User(db.Model):
    # __table__ = db.Model.metadata.tables['user']
    # extend_existing = True
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(250), nullable=True)
    forecasts = db.relationship('forecast', backref='forecasts')

    def __repr__(self):
        return '<User {}>'.format(self.user_id)


class City(db.Model):
    # __table__ = db.Model.metadata.tables['city']
    __tablename__ = 'city'
    extend_existing = True
    city_id = db.Column(db.Integer,  nullable=False, autoincrement=True, primary_key=True)
    city = db.Column(db.String(250), nullable=False)
    forecasts = db.relationship("forecast", backref='city_forecasts')

    def __repr__(self):
        return '<City {}>'.format(self.city_name)


class Forecast(db.Model):
    __tablename__ = 'forecast'
    # extend_existing = True
    __table__ = db.Model.metadata.tables['forecast']
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False,primary_key=True)
    # city = db.relationship("City", foreign_keys=[city_id])
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, primary_key=True)
    # user = db.relationship("User",  foreign_keys=[User.user_id])
    forecast_datetime = db.Column(db.DateTime, nullable=False)
    forecast = db.Column(db.Text, nullable=False)
    comment = db.Column(db.Text)

    def __repr__(self):
        return '<Forecast {}>'.format(self.forecast_id)

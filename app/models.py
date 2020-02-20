from app import db


class User(db.Model):
    __table__ = db.Model.metadata.tables['User']


class City(db.Model):
    __table__ = db.Model.metadata.tables['City']


class Forecast(db.Model):
    __table__ = db.Model.metadata.tables['Forecast']

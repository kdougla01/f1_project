from datetime import datetime
from app import db


class Team_driver(db.Model):
    # Many-to-many relationship table between Driver and Team
    __tablename__ = "team_driver"
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)


class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    teamName = db.Column(db.String(64))
    nationality = db.Column(db.String(64))
    # relationship between Team table and Driver table, reference 'team' in forms
    drivers = db.relationship('Driver', secondary="team_driver", backref='team')

    def __repr__(self):
        # specify variables to return to web page from backref
        return '{}'.format(self.teamName)


class Driver(db.Model):
    __tablename__ = "driver"
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(64))
    lastName = db.Column(db.String(64))
    raceNum = db.Column(db.Integer)
    nationality = db.Column(db.String(64))
    # relationship between Driver table and Team table, reference 'driver' in forms
    teams = db.relationship('Team', secondary="team_driver", backref='driver')

    def __repr__(self):
        # specify variables to return to web page from backref
        return '{} {}'.format(self.firstName,self.lastName)


class Calendar(db.Model):
    __tablename__ = "calendar"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(64), index=True)
    track_name = db.Column(db.String(64))
    start_date = db.Column(db.String, index=True)
    end_date = db.Column(db.String, index=True)

    def __repr__(self):
        return '{} {}'.format(self.track_name, self.end_date)
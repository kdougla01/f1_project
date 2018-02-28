from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import AddDriver, AddTeam, AddCalendar
from app.models import Driver, Team, Team_driver, Calendar


@app.route('/')
@app.route('/index')
def index():
    details = Driver.query.all()
    return render_template('index.html', title='Welcome', details=details)

@app.route('/addDriver', methods=['GET', 'POST'])
def addDriver():
    form = AddDriver()
    if form.validate_on_submit():
        # Add Driver details to Driver table in db
        driver = Driver(firstName=form.firstName.data, lastName=form.lastName.data,
                raceNum=form.raceNum.data, nationality=form.nationality.data)
        db.session.add(driver)
        db.session.commit()

        # Queries Driver table to find id of driver, filtered by race number used on driver form
        driverId = Driver.query.filter_by(raceNum=form.raceNum.data).first().id
        # Add Relationship between Driver and Team to team_driver table
        team_driver = Team_driver(team_id=form.team.data, driver_id=driverId)
        db.session.add(team_driver)
        db.session.commit()

        flash('You have successfully added a new driver')
    return render_template('addDriver.html', title='Add Driver', form=form)

@app.route('/addTeam', methods=['GET', 'POST'])
def addTeam():
    form = AddTeam()
    if form.validate_on_submit():
        team = Team(teamName=form.teamName.data,
            nationality=form.nationality.data)
        db.session.add(team)
        db.session.commit()
        flash('You have successfully added a new team')
    return render_template('addTeam.html',
                            title='Add Team',
                            form=form)

@app.route('/teamDetails', methods=['GET', 'POST'])
def teamDetails():
    details = Team.query.all()
    return render_template('teamDetails.html',  title='Team Details', details=details)

@app.route('/driverDetails', methods=['GET', 'POST'])
def driverDetails():
    details = Driver.query.all()
    return render_template('driverDetails.html',  title='Driver Details', details=details)

@app.route('/addCalendar', methods=['GET', 'POST'])
def addCalendar():
    form = AddCalendar()
    if form.validate_on_submit():
        race = Calendar(country=form.country.data, track_name=form.track_name.data, start_date=form.start_date.data, end_date=form.end_date.data)
        db.session.add(race)
        db.session.commit()
        flash('You have successfully added a new race')
    return render_template('addCalendar.html', title='Add Calendar', form=form)

@app.route('/viewCalendar', methods=['GET', 'POST'])
def viewCalendar():
    # Queries Calendar table and orders results in ascending order by start date.
    details = Calendar.query.order_by(Calendar.start_date.asc()).all()
    return render_template('calendar.html',  title='Race Calendar', details=details)
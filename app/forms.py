from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from app.models import Team

class AddDriver(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    raceNum = IntegerField('Race Number', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])

    team = SelectField(coerce=int)

    def __init__(self):
        super(AddDriver, self).__init__()
        self.team.choices = [(t.id, t.teamName) for t in Team.query.all()]

    submit = SubmitField('Submit')


class AddTeam(FlaskForm):
    teamName = StringField('Team Name', validators=[DataRequired()])
    nationality = StringField('Nationality', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddCalendar(FlaskForm):
    country = StringField('Country', validators=[DataRequired()])
    track_name = StringField('Track Name', validators=[DataRequired()])
    start_date = DateField('Start Date', format='%Y-%m-%d')
    end_date = DateField('End Date', format='%Y-%m-%d')
    submit = SubmitField('Submit')

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,IntegerField
from wtforms.validators import InputRequired,DataRequired


class PropertyForm(FlaskForm):
      title = StringField('Title', validators=[DataRequired()])
      bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])

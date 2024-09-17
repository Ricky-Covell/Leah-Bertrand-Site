from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, ColorField, IntegerRangeField, BooleanField
from wtforms.validators import DataRequired, NumberRange

class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class EditForm(FlaskForm):
    """Admin Edit Form"""

    background_color = ColorField('background_color', validators=[DataRequired()])
    background_blur = IntegerRangeField('background_blur', validators=[NumberRange(min=0, max=30, message=None)])
    inset_color = ColorField('inset_color', validators=[DataRequired()])
    soundcloud_color = IntegerRangeField('soundcloud_color', validators=[NumberRange(min=0, max=360, message=None)])
    accent_color = ColorField('accent_color', validators=[DataRequired()])
    fluid_color_1 = ColorField('fluid_color_1', validators=[DataRequired()])
    fluid_color_2 = ColorField('fluid_color_2', validators=[DataRequired()])
    fluid_color_3 = ColorField('fluid_color_3', validators=[DataRequired()])
    fluid_color_4 = ColorField('fluid_color_4', validators=[DataRequired()])
    fluid_color_5 = ColorField('fluid_color_5', validators=[DataRequired()])
    fluid_hue_rotate = IntegerRangeField('fluid_hue_rotate', validators=[NumberRange(min=0, max=360, message=None)])
    fluid_grayscale = IntegerRangeField('fluid_grayscale', validators=[NumberRange(min=0, max=100, message=None)])
    fluid_brightness = IntegerRangeField('fluid_brightness', validators=[NumberRange(min=0, max=200, message=None)])
    fluid_blur = IntegerRangeField('fluid_blur', validators=[NumberRange(min=0, max=30, message=None)])
    fluid_opacity = IntegerRangeField('fluid_opacity', validators=[NumberRange(min=0, max=100, message=None)])
    fluid_invert = BooleanField('fluid_invert')

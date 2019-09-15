from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):

    title = StringField('Pitch title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    category = SelectField('Type', choices=[('business', 'Business pitch'), (
        'Screenplay', 'Screenplay pitch'), ('project', 'Project pitch')], validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:', validators=[Required()])
    submit = SubmitField('Submit')

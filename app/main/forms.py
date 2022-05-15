from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import InputRequired

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[InputRequired()])
    comment = TextAreaField('Blog review', validators=[InputRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = SelectField('Decription', validators=[InputRequired()])
    blog = TextAreaField('Your Blog', validators=[InputRequired()])
    submit = SubmitField('Blog')
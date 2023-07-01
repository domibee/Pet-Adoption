from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators =[
                InputRequired(message="Pet needs name")])
    species = SelectField("Species", choices = [("cat","Cat"), ("dog","Dog"), ("porcupine","Porcupine")])
    img_url = StringField("Photo URL here", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    img_url = StringField("Photo URL here", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")

    def populate_obj(self, obj):
        super().populate_obj(obj)
        obj.available = self.available.dat




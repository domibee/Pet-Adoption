from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet 

from forms import AddPetForm
from forms import EditPetForm

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def homepage():
    """Get homepage with list of pets"""
    pet = Pet.query.all()
    
    return render_template('home.html', pet = pet)

@app.route('/add', methods= ["GET", "POST"])
def add_pet():
    """Get pet form and post new pet"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"{new_pet.name} added.")
        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form = form)
    
@app.route('/<int:id>', methods=["GET", "POST"])
def display_edit_pet(id):
    """Display pet info and edit form"""

    pet = Pet.query.get_or_404(id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.img_url = form.img_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('homepage'))
    
    else:
        return render_template('display_edit_pet.html', pet=pet, form = form)



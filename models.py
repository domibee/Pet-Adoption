"""Models for Adoption Agency"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMG_URL = "https://thumbs.dreamstime.com/b/cute-dog-cardboard-box-inscription-adopt-me-pet-homeless-puppy-waiting-adoption-vector-illustration-animal-234600682.jpg"

class Pet(db.Model):

    __tablename__ = 'pet'

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)
    name = db.Column(db.String, nullable = False) 
    species = db.Column(db.String, nullable = False)
    img_url = db.Column(db.Text, 
                          nullable = True,
                          default = DEFAULT_IMG_URL)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String, nullable = True)
    available = db.Column(db.Boolean, 
                          nullable = False, 
                          default = True)

    def image_url(self):
        """Return image for pet image or generic."""

        return self.img_url or DEFAULT_IMG_URL
    

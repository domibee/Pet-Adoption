from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()


woof = Pet(name = "Mr.Woof", species = "dog", age = 5, notes= "Loves cuddles", available = True)
cat = Pet(name = "Meowth", species = "cat", img_url = "https://t4.ftcdn.net/jpg/05/62/99/31/360_F_562993122_e7pGkeY8yMfXJcRmclsoIjtOoVDDgIlh.jpg", age = 8, notes = "Loves going to the beach", available = False)

db.session.add_all([woof, cat])
db.session.commit()
from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
rob = User(first_name='Robert', last_name='Leonard', image_url='https://ih1.redbubble.net/image.3236200447.2159/flat,750x,075,f-pad,750x1000,f8f8f8.jpg')
stan = User(first_name='Stanley', last_name='Clawoway', image_url='https://www.theshirtlist.com/wp-content/uploads/2023/01/Getting-Too-Old-For-This-Shit.jpg')

# Add new objects to session so they'll persist
db.session.add(rob)
db.session.add(stan)

# Commit -- otherwise, this never gets saved!
db.session.commit()
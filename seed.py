from models import User, db, Post
from app import app
from datetime import datetime

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add some users
rob = User(first_name='Robert', last_name='Leonard', image_url='https://ih1.redbubble.net/image.3236200447.2159/flat,750x,075,f-pad,750x1000,f8f8f8.jpg')
stan = User(first_name='Stanley', last_name='Clawoway', image_url='https://www.theshirtlist.com/wp-content/uploads/2023/01/Getting-Too-Old-For-This-Shit.jpg')
cory = User(first_name='C', last_name='Nektar', image_url='https://d2pxm94gkd1wuq.cloudfront.net/BreweryLogos/Standard/329206332.b.nektarmeadery.jpg')
chrissy = User(first_name='Chrissy', last_name='Oberholtzer', image_url='https://i.pinimg.com/originals/6b/fd/a2/6bfda269efa58691bb2b33ea2500e85f.jpg')
ross = User(first_name='Ross', last_name='Grounds', image_url='https://t4.ftcdn.net/jpg/05/75/07/31/360_F_575073173_SflxDglzMFPoRUfgJR1K4LkHrmiwp6zo.jpg')

# Add new objects to session so they'll persist
db.session.add_all([rob, stan, cory, chrissy, ross])

# Commit -- otherwise, this never gets saved!
db.session.commit()

now = datetime.now()

# Add some posts
p1 = Post(title='My Dog', 
          content='My dog is Laika, and she is the goodest girl',
          created_at = now,
          user_id = 1)

p2 = Post(title='This dog',
          content='My girlfriend has a dog named Max',
          created_at = now,
          user_id = 2)

p3 = Post(title='DOOM',
          content='I will be performing an MF DOOM set this Friday.',
          created_at = now,
          user_id = 2)

p4 = Post(title='Bzzzzzzz',
          content='I am the master of mead.',
          created_at = now,
          user_id = 3)

p5 = Post(title='Arcade for sale',
          content='Buy this slightly used and spilled on arcade game.',
          created_at = now,
          user_id = 1)

p6 = Post(title='Beer Guru',
          content='I juggle all the styles in my beer game.',
          created_at = now,
          user_id = 5)

p7 = Post(title='Will power',
          content='I get through the day sometimes by sheer sarcasm',
          created_at = now,
          user_id = 4)

db.session.add_all([p1, p2, p3, p4, p5, p6, p7])

# Commit -- otherwise, this never gets saved!
db.session.commit()
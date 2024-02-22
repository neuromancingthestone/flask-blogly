"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)    

class User(db.Model):
    """User model, holds first name, last name, and an image url"""

    __tablename__ = "users"

    def __repr__(self):
        u = self
        return f"<User id={u.id} first_name={u.first_name} last_name={u.last_name} image_url={u.image_url}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50), 
                          nullable=True)
    image_url = db.Column(db.String, 
                          nullable=True)

# MODELS GO BELOW!
    
    def greet(self):
        return f"Hi, I am {self.first_name} {self.last_name}!"
"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import PrimaryKeyConstraint

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
    
    post = db.relationship('Post', cascade='all, delete-orphan')

# MODELS GO BELOW!
    
    def greet(self):
        return f"Hi, I am {self.first_name} {self.last_name}!"
    
class Post(db.Model):
    """For posts"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                      nullable=False)
    content = db.Column(db.String,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False)
    
    user = db.relationship('User')
    
    assignments = db.relationship('PostTag', backref="tag", cascade='all, delete-orphan')   
    
class Tag(db.Model):
    """For Tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    
    assignments = db.relationship('PostTag', backref="post")    
    posts = db.relationship('Post', secondary="posttags", backref="tags",)
    
class PostTag(db.Model):
    """Join together Post and Tag"""
    
    __tablename__ = "posttags"

    @classmethod
    def get_is_tagged(cls, post_id, tag_id):
        if(cls.query.filter_by(post_id=post_id, tag_id=tag_id).all()):
           return True
        else:
            return False

    post_id = db.Column(db.Integer,
                        db.ForeignKey("posts.id"),
                        primary_key=True, 
                        nullable=False)
    tag_id = db.Column(db.Integer,
                       db.ForeignKey("tags.id"),
                       primary_key=True,
                       nullable=False)
    
    postref = db.relationship('Post')
    tagref = db.relationship('Tag') 
    
    __table_args__ = (
        PrimaryKeyConstraint('post_id', 'tag_id'),
    )

    
    

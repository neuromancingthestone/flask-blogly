"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "12345"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()
connect_db(app)

@app.route('/')
def home():
    """Shows home page"""
    users = User.query.all()
    return redirect('/users.html')

@app.route('/users/new.html')
def new_user():
    return render_template('new.html')

@app.route('/users/new.html', methods=["POST"])
def create_user():
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    image = request.form["image"]

    new_user = User(first_name=first_name, last_name=last_name, image_url=image)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")

@app.route('/users.html')
def list_users():
    """Shows user page"""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/users/<int:user_id>')
def show_user(user_id):
    """Show details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template('detail.html', user=user)

@app.route('/users/<int:user_id>/edit.html')
def edit_page(user_id):
    """Show details about a single pet"""
    user = User.query.get_or_404(user_id)
    return render_template('edit.html', user=user)

@app.route('/users/<int:user_id>/edit.html', methods=["POST"])
def edit_user(user_id):
    orig = User.query.get(user_id)

    orig.first_name = request.form["firstname"]
    orig.last_name = request.form["lastname"]
    orig.image_url = request.form["image"]

    db.session.add(orig)
    db.session.commit()

    return redirect(f"/users/{orig.id}")

@app.route('/users/<int:user_id>/delete.html')
def delete_user(user_id):
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect(f"/users.html")
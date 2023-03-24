from project import app
from flask import render_template, redirect, url_for
from project.models import Item, User
from project.forms import RegisterForm
from project import db

@app.route('/')
@app.route('/home')
def home_page():
    return render_template ("home.html")

@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html", items = items )

@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                              email_address=form.email_address.data, 
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if forms.errors != {}:#if there are not errors after the validation
        pass
    return render_template("register.html", form=form)

@app.route('/login')
def login_page():
    pass
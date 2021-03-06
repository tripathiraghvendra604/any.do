from app import app
from app import db, login_manager
from .forms import AnyDoForm, RegisterForm, LoginForm
from .models import AnyDo, User
from flask import redirect, render_template, flash, g
from flask.ext.login import login_user, login_required, logout_user, current_user
from functools import wraps


def logout_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user.is_authenticated:
            return redirect('/anydo')
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def get_user(id):
    user = User.query.get(id)
    return user

@app.before_request
def before_request():
    g.user = current_user


@app.route('/anydo', methods=['GET','POST'])
@login_required
def index():
    form = AnyDoForm()

    if form.validate_on_submit():
        print 'form validate'
        x = AnyDo(
            body = form.body.data
        )
        db.session.add(x)
        db.session.commit()
        print 'added Any.Do'
        return redirect('/anydo')
    else:
        print 'error here'
    return render_template('anydo.html', form=form)


@app.route('/register', methods=['Get', 'POST'])
@logout_required
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registered Successfully')
        return redirect('/login')
    return render_template('register.html', form = form)


@app.route('/login', methods=['GET', "POST"])
@logout_required
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect('/anydo')
            else:
                return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    g.user = None
    return redirect('/login')

@app.route('/list')
@login_required
def list():
    list = AnyDo.query.all()
    return  render_template('list.html', list=list)

@app.route('/delete/<id>')
def delete(id):
    ele = AnyDo.query.get(id)
    db.session.delete(ele)
    db.session.commit()
    return redirect('/list')
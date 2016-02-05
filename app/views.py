from app import app
from app import db
from .forms import AnyDoForm, RegisterForm
from .models import AnyDo, User
from flask import redirect, render_template, flash


@app.route('/anydo', methods=['GET','POST'])
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
    return render_template('register.html', form = form)
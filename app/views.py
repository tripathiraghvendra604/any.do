from app import app
from app import db
from .forms import AnyDoForm
from .models import AnyDo, User
from flask import redirect, render_template


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

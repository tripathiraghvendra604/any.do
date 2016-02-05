from app import db

class AnyDo(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    body = db.Column(db.String(300))
    #user = db.Column(db.ForeignKey('user.id'))

    def __repr__(self):
        return '<DO %s>' %self.body

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(20))
    email = db.Column(db.String(200))

    def __repr__(self):
        return '<User %s>' %self.name
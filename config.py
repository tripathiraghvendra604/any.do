import os

path=os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.join(path, 'app.db')

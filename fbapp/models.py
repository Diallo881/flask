from flask_sqlalchemy import SQLAlchemy

from .views import app
import enum
import logging as lg

# Create database connection object
db = SQLAlchemy(app)

# Créer la table Gender
class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2

# Créer la table Content
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender

db.create_all()

# Initialiser la db
def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("THIS IS SPARTAAAAAAA!!!", Gender['male']))
    db.session.add(Content("What's your favorite scary movie?", Gender['female']))
    db.session.commit()
    lg.warning('Database initialized!')
    
    

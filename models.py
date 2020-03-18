from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.model):

    __tablename__ = "users"
    email = db.Column(db.String(50), primary_key=Ture, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    mobile = db.Column(db.String(30))
    institution = db.Column(db.String(50))
    designation = db.Column(db.String(30))

    db.create_all()
    

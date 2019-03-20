from sqlalchemy.sql import func
from config import db
class Dojo(db.Model):	
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(45), nullable=False)
    city = db.Column(db.String(45), nullable=False)
    state = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

class Ninja(db.Model):	
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(45), nullable=False) 
    last_name = db.Column(db.String(45), nullable=False)
    dojo_id = db.Column(db.Integer, db.ForeignKey('dojo.id'), nullable=False,)
    dojo = db.relationship('Dojo', foreign_keys=[dojo_id], backref='ninjas', cascade='all')
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
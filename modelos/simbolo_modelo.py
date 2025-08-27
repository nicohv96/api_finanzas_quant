from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

from app import app, db       

class Symbol(db.Model): 
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(100))
    simbolo=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,simbolo,imagen):
        self.nombre=nombre 
        self.simbolo=simbolo
        self.imagen=imagen

with app.app_context():
    db.create_all() 


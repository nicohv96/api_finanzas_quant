from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

from app import app, db 

class User(db.Model):  
    id=db.Column(db.Integer, primary_key=True)
    usuario=db.Column(db.String(100))
    passw=db.Column(db.String(100))
    estado=db.Column(db.Boolean, default=False)
    def __init__(self,usuario,passw,estado=False):
        self.usuario=usuario 
        self.passw=passw
        self.estado=estado

with app.app_context():
    db.create_all() 

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

from app import app, db          #,ma

# defino las tablas
class Symbol(db.Model):   # la clase Simbolos hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    simbolo=db.Column(db.String(100))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,simbolo,imagen): #crea el  constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.nombre=nombre 
        self.simbolo=simbolo
        self.imagen=imagen

#  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************

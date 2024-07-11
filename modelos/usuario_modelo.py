from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

from app import app, db          #,ma

# defino las tablas
class User(db.Model):   # la clase Simbolos hereda de db.Model de SQLAlquemy   
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    usuario=db.Column(db.String(100))
    passw=db.Column(db.String(100))
    estado=db.Column(db.Boolean, default=False)
    def __init__(self,usuario,passw,estado=False): #crea el  constructor de la clase
        # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.usuario=usuario 
        self.passw=passw
        self.estado=estado

#  si hay que crear mas tablas , se hace aqui

with app.app_context():
    db.create_all()  # aqui crea todas las tablas si es que no estan creadas
#  ************************************************************

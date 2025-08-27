from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:algundia96@localhost/db_finanzas_quant'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)

from controladores.simbolo_controlador import *
from controladores.usuario_controlador import *

if __name__=='__main__':  
    app.run(debug=True, port=5000)


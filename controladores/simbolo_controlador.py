from flask import  jsonify,request  #,Flask# del modulo flask importar la clase Flask y los métodos jsonify,request

from app import app, db, ma   # del modulo app.py  importa el objeto app, db, ma

from modelos.simbolo_modelo import *

class SymbolSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','simbolo','imagen')


symbol_schema=SymbolSchema()  # El objeto producto_schema es para traer un producto
symbols_schema=SymbolSchema(many=True)  # El objeto productos_schema es para traer multiples registros de producto

# crea los endpoint o rutas (json)
@app.route('/simbolos',methods=['GET'])
def get_symbols():
    all_symbols=Symbol.query.all() # el metodo query.all() lo hereda de db.Model
    result=symbols_schema.dump(all_symbols)  #el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)     # retorna un JSON de todos los registros de la tabla

@app.route('/simbolos/<id>',methods=['GET'])
def get_symbol(id):
    symbol=Symbol.query.get(id)
    return symbol_schema.jsonify(symbol)   # retorna el JSON de un producto recibido como parametro

@app.route('/simbolos/<id>',methods=['DELETE'])
def delete_symbol(id):
    symbol=Symbol.query.get(id)
    db.session.delete(symbol)
    db.session.commit()                     # confirma el delete
    return symbol_schema.jsonify(symbol) # me devuelve un json con el registro eliminado

@app.route('/simbolos', methods=['POST']) # crea ruta o endpoint
def create_symbol():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    simbolo=request.json['simbolo']
    imagen=request.json['imagen']
    new_symbol=Symbol(nombre,simbolo,imagen)
    db.session.add(new_symbol)
    db.session.commit() # confirma el alta
    return symbol_schema.jsonify(new_symbol)

@app.route('/simbolos/<id>' ,methods=['PUT'])
def update_symbol(id):
    symbol=Symbol.query.get(id)
 
    symbol.nombre=request.json['nombre']
    symbol.simbolo=request.json['simbolo']
    symbol.imagen=request.json['imagen']
    db.session.commit()    # confirma el cambio
    return symbol_schema.jsonify(symbol)    # y retorna un json con el producto

@app.route('/')
def bienvenida():
    return "Bienvenidos al backend"   # retorna el JSON de un usuario recibido como parametro
from flask import jsonify, request, make_response
from app import app, db, ma
from modelos.usuario_modelo import User
from functools import wraps

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'usuario', 'passw', 'estado')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = data.get('usuario')
    passw = data.get('passw')
    
    existing_user = User.query.filter_by(usuario=usuario).first()
    if existing_user:
        return make_response(jsonify({"message": "User already exists"}), 400)
    
    new_user = User(usuario, passw, estado=False)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully"}), 201

# Endpoint para autenticación
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    passw = data.get('passw')
    
    user = User.query.filter_by(usuario=usuario, passw=passw).first()
    
    if user:
        if user.estado==1:
            return jsonify({"message": "Login successful"}), 200
        else:
            return make_response(jsonify({"message": "User account disabled"}), 403)
    else:
        return make_response(jsonify({"message": "Invalid credentials"}), 401)

# Endpoints CRUD para usuarios con protección
@app.route('/usuarios', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/usuarios/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/usuarios/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@app.route('/usuarios', methods=['POST'])
def create_user():
    usuario = request.json['usuario']
    passw = request.json['passw']
    estado = request.json['estado']
    new_user = User(usuario, passw, estado)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/usuarios/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    user.usuario = request.json['usuario']
    user.passw = request.json['passw']
    user.estado = request.json['estado']
    db.session.commit()
    return user_schema.jsonify(user)

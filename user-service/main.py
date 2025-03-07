from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from flask_cors import CORS  # Importation de CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo-service:27017/users_db'
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
CORS(app)  # Active CORS pour toutes les routes, autorise toutes les origines par défaut

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password are required"}), 400
    
    if mongo.db.users.find_one({"username": data['username']}):
        return jsonify({"message": "Username already exists"}), 409
    
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = {"username": data['username'], "password": hashed_password}
    mongo.db.users.insert_one(user)
    return jsonify({"message": "User created successfully"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username and password are required"}), 400
    
    user = mongo.db.users.find_one({"username": data['username']})
    if user and bcrypt.check_password_hash(user['password'], data['password']):
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

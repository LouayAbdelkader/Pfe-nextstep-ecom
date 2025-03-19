import os
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from bson import ObjectId
from pymongo.errors import PyMongoError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "louaymoncef")  # Required for CSRF protection
app.config['MONGO_URI'] = os.getenv("MONGO_URI", "mongodb://mongo-service:27017/products_db")
mongo = PyMongo(app)

# Enable CSRF protection
csrf = CSRFProtect()
csrf.init_app(app)

# Configure CORS with dynamic origins
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
CORS(app, resources={
    r"/*": {
        "origins": allowed_origins,
        "methods": ["GET", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

@app.route("/products", methods=["GET"])
def get_products():
    try:
        products = mongo.db.products.find()
        return jsonify({
            "products": [
                {
                    "id": str(p["_id"]),
                    "name": p["name"],
                    "description": p.get("description", "No description available"),
                    "price": p.get("price", 0)
                } for p in products
            ]
        })
    except PyMongoError as e:
        return jsonify({"message": "Database error", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

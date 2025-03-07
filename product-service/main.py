from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS  # Importation de CORS

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://mongo-service.dev.svc.cluster.local:27017/products_db'
mongo = PyMongo(app)
CORS(app)  # Active CORS pour toutes les routes

@app.route("/products", methods=["GET"])
def get_products():
    products = mongo.db.products.find()
    # Renvoie tous les champs sauf '_id', qui est converti en chaîne si nécessaire
    return jsonify({
        "products": [
            {
                "name": p["name"],
                "description": p.get("description", "No description available"),
                "price": p.get("price", 0)  # Valeur par défaut si le champ est absent
            } for p in products
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)



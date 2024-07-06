
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://db:27017/mydatabase"
mongo = PyMongo(app)
CORS(app)

@app.route('/')
def hello():
    return "Hello from backend"

@app.route('/test-db')
def test_db():
    item = {"name": "Test Item"}
    mongo.db.items.insert_one(item)
    items = list(mongo.db.items.find({}, {"_id": 0}))
    return jsonify(items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

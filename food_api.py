from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def load_food_records():
    with open("food_records.json", "r", encoding="utf-8") as file:
        return json.load(file)

@app.route("/")
def home():
    return "Food Safety API is running."

@app.route("/api/foods", methods=["GET"])
def get_foods():
    foods = load_food_records()
    return jsonify(foods)

@app.route("/api/foods/<product_id>", methods=["GET"])
def get_food_by_id(product_id):
    foods = load_food_records()
    for food in foods:
        if food["product_id"] == product_id:
            return jsonify(food)
    return jsonify({"error": "Product not found"}), 404

@app.route("/api/foods/search", methods=["GET"])
def search_foods():
    status = request.args.get("status")
    category = request.args.get("category")

    foods = load_food_records()

    if status:
        foods = [food for food in foods if food["safety_status"].lower() == status.lower()]

    if category:
        foods = [food for food in foods if food["category"].lower() == category.lower()]

    return jsonify(foods)
from flask import Blueprint, request, jsonify
from app.utils import load_products, save_products
from app.models import Product

product_bp = Blueprint("products", __name__)

# GET /products
@product_bp.route("/products", methods=["GET"])
def get_products():
    products = load_products()
    return jsonify(products)

# GET /product/<id>
@product_bp.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

# POST /product/<id>
@product_bp.route("/product/<int:product_id>", methods=["POST"])
def add_product(product_id):
    products = load_products()
    data = request.json
    new_product = Product(id=product_id, name=data["name"], price=data["price"])
    products.append(new_product.to_dict())
    save_products(products)
    return jsonify(new_product.to_dict()), 201

# PUT/PATCH /product/<id>
@product_bp.route("/product/<int:product_id>", methods=["PUT", "PATCH"])
def update_product(product_id):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            p["name"] = request.json.get("name", p["name"])
            p["price"] = request.json.get("price", p["price"])
            save_products(products)
            return jsonify(p)
    return jsonify({"error": "Product not found"}), 404

# DELETE /product/<id>
@product_bp.route("/product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    products = load_products()
    for p in products:
        if p["id"] == product_id:
            products.remove(p)
            save_products(products)
            return jsonify({"message": "Deleted successfully"})
    return jsonify({"error": "Product not found"}), 404

# Tìm kiếm theo tên
@product_bp.route("/products/search", methods=["GET"])
def search_products():
    query = request.args.get("q", "").lower()
    products = load_products()
    results = [p for p in products if query in p["name"].lower()]
    return jsonify(results)
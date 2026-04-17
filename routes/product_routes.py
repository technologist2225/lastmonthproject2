from flask import Blueprint, request, jsonify
from managers.product_manager import ProductManager

product_bp = Blueprint('product_bp', __name__)
pm = ProductManager()

@product_bp.route('/products', methods=['GET'])
def get_products():
    args = request.args
    # Nếu có query parameters (vd: ?name=Ao), gọi hàm search
    if args:
        results = pm.search_product(args)
        return jsonify({"message": "Kết quả tìm kiếm", "data": results}), 200
    
    # Nếu không có query, trả về toàn bộ
    return jsonify({"message": "Danh sách sản phẩm", "data": pm.get_all()}), 200

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    required_fields = ["spid", "name", "price", "quantity"]
    
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Thiếu thông tin sản phẩm"}), 400
        
    success, result = pm.add_product(data["spid"], data["name"], data["price"], data["quantity"])
    if success:
        return jsonify({"message": "Thêm thành công", "data": result}), 201
    return jsonify({"error": result}), 400

@product_bp.route('/products/<spid>', methods=['PUT'])
def update_product(spid):
    data = request.json
    updated_sp = pm.update_product(spid, data)
    
    if updated_sp:
        return jsonify({"message": "Cập nhật thành công", "data": updated_sp}), 200
    return jsonify({"error": "Không tìm thấy sản phẩm"}), 404

@product_bp.route('/products/<spid>', methods=['DELETE'])
def delete_product(spid):
    if pm.delete_product(spid):
        return jsonify({"message": "Xóa thành công"}), 200
    return jsonify({"error": "Không tìm thấy sản phẩm"}), 404
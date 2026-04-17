# Product Management API (Flask + JSON)

Dự án API Quản lý Sản phẩm sử dụng Python Flask, kiến trúc Blueprint và lưu trữ dữ liệu tạm thời bằng file `product.json`.

## Cài đặt và Khởi chạy
1. Cài đặt thư viện: `pip install flask`
2. Chạy server: `python app.py`
3. Server sẽ chạy tại: `http://localhost:5000/api`

## Test Bằng Postman

### 1. Lấy danh sách sản phẩm (GET)
* **URL:** `GET http://localhost:5000/api/products`

### 2. Thêm sản phẩm mới (POST)
* **URL:** `POST http://localhost:5000/api/products`
* **Body (raw -> JSON):**
  ```json
  {
      "spid": "SP01",
      "name": "Laptop Dell",
      "price": 1500.5,
      "quantity": 10
  }
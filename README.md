Product Manager API (Flask)

Giới thiệu

Dự án này là một API quản lý sản phẩm viết bằng Flask, dữ liệu được lưu trong file JSON. API hỗ trợ các chức năng CRUD và tìm kiếm theo tên.

Cài đặt

Clone repo về máy:

git clone cd product_manager

Cài đặt thư viện:

python -m pip install -r requirements.txt

Chạy server

python run.py

Server sẽ chạy tại http://127.0.0.1:5000.

Các endpoint

GET /products → Xem danh sách sản phẩm

GET /product/ → Xem chi tiết sản phẩm

POST /product/ → Thêm sản phẩm (Body JSON: { "name": "Laptop Dell", "price": 1500 })

PUT /product/ → Sửa sản phẩm

DELETE /product/ → Xóa sản phẩm

GET /products/search?q=<tên> → Tìm kiếm sản phẩm theo tên

Demo

Dùng Postman để test các API.

Quay video demo quá trình thêm, sửa, xóa, tìm kiếm sản phẩm.

Upload video lên YouTube/Google Drive và chèn link tại đây.

Ghi chú

Đây là server Flask chạy ở chế độ development, không dùng cho production.

Dữ liệu được lưu trong file products.json ngay tại thư mục dự án.

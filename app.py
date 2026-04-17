from flask import Flask
from routes.product_routes import product_bp

app = Flask(__name__)

app.register_blueprint(product_bp, url_prefix='/api')

if __name__ == '__main__':
    print("~~\/\/\/\~~ Server Quản Lý Sản Phẩm Đang Chạy ~~\/\/\/\/~~")
    app.run(debug=True, port=5000)              
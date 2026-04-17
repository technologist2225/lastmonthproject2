import json
import os

from models.product import Product


class ProductManager:
    def __init__(self):
        self.products = []
        self.file_path = "product.json"
        self.load_json()

    def load_json(self):
        if not os.path.exists(self.file_path):
            self.save_json()
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.products = []
            for item in data:
                sp = Product(item["spid"], item["name"], item["price"], item["quantity"])
                self.products.append(sp)
        except:
            self.products = []

    def save_json(self):
        data = [sp.to_dict() for sp in self.products]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_all(self):
        return [sp.to_dict() for sp in self.products]

    def add_product(self, spid, name, price, quantity):
        # Kiểm tra trùng lặp ID
        for sp in self.products:
            if sp.spid == spid:
                return False, "Mã sản phẩm đã tồn tại!"
       
        new_sp = Product(spid, name, price, quantity)
        self.products.append(new_sp)
        self.save_json()
        return True, new_sp.to_dict()

    def update_product(self, spid, update_data):
        for sp in self.products:
            if sp.spid == spid:
                if "name" in update_data:
                    sp.name = update_data["name"]
                if "price" in update_data:
                    sp.price = float(update_data["price"])
                if "quantity" in update_data:
                    sp.quantity = int(update_data["quantity"])
                self.save_json()
                return sp.to_dict()
        return None

    def delete_product(self, spid):
        for sp in self.products:
            if sp.spid == spid:
                self.products.remove(sp)
                self.save_json()
                return True
        return False

    def search_product(self, filters):
        results = self.products
        if "spid" in filters:
            results = [sp for sp in results if sp.spid == filters["spid"]]
        if "name" in filters:
            results = [sp for sp in results if filters["name"].lower() in sp.name.lower()]
        if "min_price" in filters and "max_price" in filters:
            results = [sp for sp in results if float(filters["min_price"]) <= sp.price <= float(filters["max_price"])]
        if "quantity" in filters:
            results = [sp for sp in results if sp.quantity == int(filters["quantity"])]
       
        return [sp.to_dict() for sp in results]
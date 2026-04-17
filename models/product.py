class Product:
    def __init__(self, spid, name, price, quantity):
        self.spid = spid
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def to_dict(self):
        return {
            "spid": self.spid,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity 
        }
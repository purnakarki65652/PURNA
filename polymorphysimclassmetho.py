class Amazon:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print(f"This is product and am class is invoked.The name is {self.name}.This costs {self.price} rupees.")
class Flipkart:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def info(self):
        print(f"This is product and fli class is invoked. The name is {self.name}. This cost {self.price}.")
FLP = Flipkart("Iphone", 2.5)
AMZ = Amazon("Iphone",4)
for product1 in (FLP,AMZ):
    product1.info()

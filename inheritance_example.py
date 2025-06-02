class Product:
    def __init__(self,name,price,quantity):
        self.price=price
        self.name=name
        self.quantity=quantity
    def get_price(self):
        return self.price * self.quantity
    
    def displayinfo(self):
        print(f"Product name :",{self.name})
        print(f"Product price :", {self.price})
        print(f"Product quantity :", {self.quantity})
        print(f"Product price :", {self.get_price()})
class TV(Product):
    def __init__(self,name,price,quantity,warenty):
        super().__init__(name,price,quantity)
        self.warenty=warenty
    def displayinfo(self):
        super().displayinfo()
        print(f"Product Warenty:",{self.warenty})
class Washingmachine(Product):
    def __init__(self,name,price,quantity,brand):
        super.__init__(name,price,quantity)
        self.brand=brand
    def displayinfo(self):
        super().displayinfo()
        print(f"Product brand:",{self.brand})

t=TV("samsung",19000,2,"2 years")
t.displayinfo()


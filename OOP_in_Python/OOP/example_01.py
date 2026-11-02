class shop:
    def __init__(self, product, price):
        self.product=product
        self.price=price
        
    def get_info(self):
        print(f"your {self.product} price is {self.price} taka.")
        
    def calc_discount(self,discount):
        final_price=self.price-(self.price*discount/100)
        print(f"your final price after discount is {final_price}")
        
        
#=========================================================================
p1=shop("phone", 35000)
p1.get_info()
p1.calc_discount(20) 
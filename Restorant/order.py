class Order:
    def __init__(self, f_id=0, f_name="", f_price=0):
        self.f_id = f_id
        self.f_name = f_name
        self.f_price = f_price
        
    def __str__(self):
        return f"{self.f_id},{self.f_name},{self.f_price}"

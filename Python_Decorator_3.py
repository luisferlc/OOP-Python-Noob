class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def rating(self, new_price):
        if isinstance(new_price, float) and new_price > 0:
            self._price = new_price
        else:
            print("Enter a valid price.")
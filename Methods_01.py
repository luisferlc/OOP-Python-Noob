class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_diameter(self):
        #return self.radius * 2
        print(f"Diameter: {self.radius * 2}")
        

circle_1 = Circle(5)
#print(circle_1.calculate_diameter())
circle_1.calculate_diameter()

##################################################################

class Backpack:

    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        return self._items
    
    def add_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Provide a valid item.")
    
    def remove_items(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items
        
mochila_del_nata = Backpack()
print(mochila_del_nata.has_item("Lapiz"))
mochila_del_nata.add_items("Lapiz")
mochila_del_nata.add_items("Crayon")
mochila_del_nata.add_items("Borrador")
print(mochila_del_nata.items)
mochila_del_nata.remove_items("JE")
mochila_del_nata.remove_items("Borrador")
print(mochila_del_nata.items)
print(mochila_del_nata.has_item("Crayon"))

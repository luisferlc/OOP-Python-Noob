class Circle:
    
    VALID_COLORS = ("Red","Blue","Green") #A constant. En mayusculas, esta variable convncionalmente es una constante. tuple para que no la modifiquen.
    
    def __init__(self, color, radius):
        self._color = color
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Not a valid new radius.")
    
    radius = property(get_radius ,set_radius)

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Not a valid color.")



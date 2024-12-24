#class Dog:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def get_age(self):
#        return self.age
#    
#    def set_age(self, new_age):
#        if isinstance(new_age, int) and 0 < new_age < 30:
#            self.age = new_age
#        else:
#            print("Enter a valid age.")

# Imagina que te piden hacer non-public el atributo age, y ya tienes miles de líneas de código donde usas eesee atributo.
# En lugar de modificar todo el proyecto, puedes crear una propiedad:

# Primero haces non-public el atributo, y al final defines la propiedad:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        print("Calling getter")
        return self._age
    
    def set_age(self, new_age):
        print("Calling setter")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print("Enter a valid age.")

    age = property(get_age, set_age) # Property


my_dog = Dog("Manin", 9)
print(f"My dog is {my_dog.age} years old.")

my_dog.age += 1
print(f"My dog is now {my_dog.age} years old.")

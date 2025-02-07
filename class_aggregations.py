class Vehicle():
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def show_info(self):
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")


class Employee():
    def __init__(self, name, age, carro):
        self.name = name
        self.age = age
        self.carro = carro

    def show_info(self):
        self.carro.show_info()


mi_carrito = Vehicle("Rojo",2019) #creas una instancia de Vehicle
luison = Employee("Luis",31, mi_carrito) #la utilizar como parametro para otra instancia de otra clase

luison.carro.show_info()
print(luison.carro.color)
print(luison.carro.model)




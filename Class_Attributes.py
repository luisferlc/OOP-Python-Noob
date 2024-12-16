## Class attributes vs Instance attributes:

class Dog:

    species = "Canis Lupus" #class attribute, todas las instancias de esta clase, compartiran este valor.

    def __init__(self, name, age, breed): #instance attributes, difieren entre cada instancia.
        self.name = name
        self.age = age
        self.breed = breed

class Backpack:

    max_num_items = 10

    def __init__(self):
        self.items = []

class Movie: #Cada instancia va tener un ID unico, eel cual see ira incrementando a medida que se creen nuevas instancias.

    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1

movie_1 = Movie("JEEJEE",10)
movie_2 = Movie("JIJI",9)
movie_3 = Movie("JOJO",5)

print(movie_1.id)
print(movie_2.id)
print(movie_3.id)
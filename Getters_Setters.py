# get_: para printear atributos
# set_: para modificar atributos

####### get_
class Movie:
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title

my_movie = Movie("007", 4.5)

print("My fav movie:",my_movie.get_title())

####### set_
class Dog:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print("Enter a valid name.")

my_dog = Dog("Panfilo", 5)
print(my_dog.get_name())
my_dog.set_name("Panfilito")
print(my_dog.get_name())
my_dog.set_name("Panfilito2")
print(my_dog.get_name())
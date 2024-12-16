class Circle:
    def __init__(self, radius=5):
        self.radius = radius
        self.color = "Blue" #fixed value

class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Movie:
    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating= rating


movie1 = Movie("Harry Puter", 1969, "Espanglish", 100)
print(movie1.title)
print(movie1.year)
print(movie1.language)
print(movie1.rating)

my_circle = Circle() #With default value
print("\n Default value:",my_circle.radius)
my_circle_1 = Circle(10) #Modifying radius value
print(my_circle_1.radius)

##### Syntax error: cuando defines un atributo con un valor deefault, estos tienen que ir al final de la definición en tu clase
### MAL:
#class Ejemplo:
#    def __init__(self, color="Blue", size): #porque causaria problemas al momento de crear una instancia de esa clase, si es que quieres
#        self.color = color                  # utilizar el valor default
#        self.size = size
### BIEN:
class Ejemplo:
    def __init__(self, size, color="Blue"):
        self.color = color
        self.size = size


#### Updating attributes
#movie1
print("\nUpdating class attributes")
movie1.language = "Deutshhh"
movie1.title = "Not Harry Puter anymore"
movie1.rating = 5
movie1.year = 2024
print(movie1.title)
print(movie1.year)
print(movie1.language)
print(movie1.rating)

### Delete attributes
# two ways
#print(movie1.title)
#del movie1.title
#print(movie1.title)
###
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

player = Player(5,10)
#print(player.x, player.y)

attributes = ["x","y"]
for attribute in attributes:
    delattr(player, attribute)

#print(player.x, player.y)
#### Default Arguments

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change

my_player = Player(10,5)
print(my_player.x)
print(my_player.y)
my_player.move_up()
my_player.move_left()
print(my_player.x)
print(my_player.y)
my_player.move_up(100)
my_player.move_left(50)
print(my_player.x)
print(my_player.y)

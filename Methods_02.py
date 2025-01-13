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

##############################################
##############################################

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

    def show_items(self, sort_list=False):
        if sort_list:
            print(sorted(self._items))
        else:
            print(self._items)

mochila_del_nata = Backpack()
mochila_del_nata.add_items("Lapiz")
mochila_del_nata.add_items("Crayon")
mochila_del_nata.add_items("Borrador")
print("Not sorted:")
mochila_del_nata.show_items()
print("Sorted:")
mochila_del_nata.show_items(True)
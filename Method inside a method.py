class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    #Add multiple items, recycle add_item method:
    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Provide a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items

bp = Backpack()
print(bp.items)
bp.add_multiple_items(["Crayon", "Lapiz", "Borrador"])
print(bp.items)
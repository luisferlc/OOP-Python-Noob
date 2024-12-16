class Bacteria:
    def __init__(self, x, y, tipo, alimentacion, flagelo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.alimentacion = alimentacion
        self.flagelo = flagelo

# Tipos: cocos, bacilos, helicoidales
# Alimentacion: autotrofas, heterotrofas
# Flagelo: fimbrias,fili

bac1 = Bacteria(4, 3, "cocos", "autotrofas", "fimbrias")
bac2 = Bacteria(6, 5, "bacilos", "heterotrofas", "fimbrias")
bac3 = Bacteria(2, 3, "helicoidales", "heterotrofas", "fili")
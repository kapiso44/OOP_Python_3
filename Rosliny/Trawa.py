from Rosliny.Roslina import Roslina


class Trawa(Roslina):

    def __init__(self, miejsce, swiat):
        super(Trawa, self).__init__("Trawa", miejsce, 0, 0, "T", "lightgreen", swiat)

    def stworzdziecko(self, p):
        return Trawa(p, self.swiat)

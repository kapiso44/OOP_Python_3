from Zwierzeta.Zwierze import Zwierze


class Wilk(Zwierze):

    def __init__(self, miejsce, swiat):
        super(Wilk, self).__init__("Wilk", miejsce, 9, 5, "W", "black", swiat)

    def stworzdziecko(self, p):
        return Wilk(p, self.swiat)

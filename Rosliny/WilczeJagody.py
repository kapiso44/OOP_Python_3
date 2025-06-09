from Rosliny.Roslina import Roslina


class WilczeJagody(Roslina):

    def __init__(self, miejsce, swiat):
        super(WilczeJagody, self).__init__("Wilcze Jagody", miejsce, 99, 0, "X", "purple", swiat)

    def stworzdziecko(self, p):
        return WilczeJagody(p, self.swiat)

    def czyZjadlSpecjalna(self, jedzacy):
        self.zyje = False
        self.swiat.setPolePlanszy(self.lokacja, None)
        return True

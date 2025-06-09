from Rosliny.Roslina import Roslina


class WilczeJagody(Roslina):

    def __init__(self, miejsce, swiat):
        super(WilczeJagody, self).__init__("Wilcze Jagody", miejsce, 99, 0, "X", "purple", swiat)

    def stworzdziecko(self, p):
        return WilczeJagody(p, self.swiat)

    def kolizja(self, atakujacy):
        self.swiat.dodajWpis(f"{self} otruł {atakujacy}")
        atakujacy.setZyje(False)
        self.swiat.setPolePlanszy(atakujacy.getLokacja(), None)
        self.zyje = False
        self.swiat.setPolePlanszy(self.lokacja, None)

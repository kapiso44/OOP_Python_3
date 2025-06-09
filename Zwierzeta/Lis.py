from Zwierzeta.Zwierze import Zwierze


class Lis(Zwierze):

    def __init__(self, miejsce, swiat):
        super(Lis, self).__init__("Lis", miejsce, 3, 7, "L", "orange", swiat)

    def stworzdziecko(self, p):
        return Lis(p, self.swiat)

    def atakowanie(self, atakowany):
        if atakowany.getSila() < self.sila:
            super(Lis, self).atakowanie(atakowany)
        else:
            self.swiat.dodajWpis(f"{self} wyczuł {atakowany}")

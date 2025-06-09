import random

from Zwierzeta.Zwierze import Zwierze


class Zolw(Zwierze):

    def __init__(self, miejsce, swiat):
        super().__init__("Żółw", miejsce, 2, 1, "Z", "darkgreen", swiat)

    def stworzdziecko(self, p):
        return Zolw(p, self.swiat)

    def akcja(self):
        if random.randint(0, 4) == 0:
            super(Zolw, self).akcja()
        else:
            self.swiat.dodajWpis(f"{self} nie poruszył się")

    def czyOdbilAtak(self, atakujacy):
        return atakujacy.getSila() < 5

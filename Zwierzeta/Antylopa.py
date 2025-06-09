import random

from Zwierzeta.Zwierze import Zwierze


class Antylopa(Zwierze):

    def __init__(self, miejsce, swiat):
        super(Antylopa, self).__init__("Antylopa", miejsce, 4, 4, "A", "pink", swiat)

    def stworzdziecko(self, p):
        return Antylopa(p, self.swiat)

    def akcja(self):
        cel = self.losujRuch(self.lokacja, 2)
        self.swiat.dodajWpisAkcja(self, cel)
        self.kolizja(cel)

    def atakowanie(self, atakowany):
        if random.randint(0, 1) == 0:
            self.swiat.dodajWpis(f"{self} nie udało się uciec przed {atakowany}")
            super(Antylopa, self).atakowanie(atakowany)
        else:
            self.swiat.dodajWpis(f"{self} chce uciec przed zaatakowaniem {atakowany}")
            p = self.swiat.sprawdzMiejsce(atakowany.getLokacja())
            if p is not None:
                self.swiat.dodajWpisAkcja(self, p)
                self.kolizja(p)
            else:
                self.swiat.dodajWpis(f"{self} nie może uciec przed {atakowany}")
                super(Antylopa, self).atakowanie(atakowany)

    def czyUniknalAtak(self, atakujacy):
        if random.randint(0, 1) == 0:
            self.swiat.dodajWpis(f"{self} nie udało się uciec przed {atakujacy}")
            return False
        else:
            self.swiat.dodajWpis(f"{self} chce uciec przed atakującym {atakujacy}")
        p = self.swiat.sprawdzMiejsce(self.lokacja)
        if p is not None:
            self.swiat.dodajWpisAkcja(self, p)
            temp = self.lokacja
            self.kolizja(p)
            atakujacy.kolizja(temp)
            return True
        else:
            self.swiat.dodajWpis(f"{self} nie może uciec przed {atakujacy}")
            return False

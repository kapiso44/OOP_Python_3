import random
from abc import ABC

from Organizm import Organizm


class Roslina(Organizm, ABC):

    def __init__(self, nazwa, miejsce, sila, inicjatywa, znak, kolor, swiat):
        super(Roslina, self).__init__(nazwa, miejsce, sila, inicjatywa, znak, kolor, swiat)

    def akcja(self):
        if random.randint(0, 25) == 0 and self.narodzony is False:
            p = self.swiat.sprawdzMiejsce(self.lokacja)
            if p is not None:
                dziecko = self.stworzdziecko(p)
                dziecko.setNarodzony(True)
                self.swiat.dodajOrganizm(dziecko)
                self.swiat.dodajWpis(f"{self} zasiał się")
        else:
            self.swiat.dodajWpis(f"{self} nie zasiał się")

    def kolizja(self, atakujacy):
        if self.czyZjadlSpecjalna(atakujacy):
            self.swiat.dodajWpis(f"{atakujacy} doznał efektu od {self}")
        self.swiat.dodajWpis(f"{atakujacy} zjadł {self}")
        self.zyje = False
        self.swiat.setPolePlanszy(self.lokacja, None)

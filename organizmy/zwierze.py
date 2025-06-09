from abc import ABC
from .organizm import Organizm


class Zwierze(Organizm, ABC):
    def __init__(self, nazwa, miejsce, sila, inicjatywa, znak, kolor, swiat):
        super(Zwierze, self).__init__(nazwa, miejsce, sila, inicjatywa, znak, kolor, swiat)

    def akcja(self):
        cel = self.losujRuch(self.lokacja, 1)
        self.swiat.dodajWpisAkcja(self, cel)
        self.kolizja(cel)

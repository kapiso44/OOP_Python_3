import random

from Punkt import Punkt
from Swiat import Swiat


class MenedzerSave:
    swiat = None

    def __init__(self, swiat):
        self.swiat = swiat

    def generujGre(self, rozmiarX, rozmiarY, ilosc):
        self.swiat = Swiat(rozmiarX, rozmiarY)

        self.swiat.dodajOrganizmMod("C", Punkt(int(rozmiarX / 2), int(rozmiarY / 2)), -1, -1, -1)

        gatunki = ["W", "O", "L", "Z", "A", "R", "T", "M", "G", "B", "X"]
        for x in range(ilosc - 1):
            index = random.randint(0, len(gatunki) - 1)
            p = Punkt(int(rozmiarX / 2), int(rozmiarY / 2))
            while self.swiat.getPolePlanszy(p) is not None:
                p = Punkt(random.randint(0, rozmiarX - 1), random.randint(0, rozmiarY - 1))
            self.swiat.dodajOrganizmMod(gatunki[index], p, -1, -1, -1)

        return self.swiat

    def zapiszGre(self, nazwapliku):
        if self.swiat is None:
            return
        self.swiat.zapisz_stan(nazwapliku)

    def wczytajGre(self, nazwapliku):
        self.swiat = Swiat.wczytaj_stan(nazwapliku)
        return self.swiat

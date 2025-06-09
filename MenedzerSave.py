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
        f = open(nazwapliku, "w")

        f.write(f"{self.swiat.getRozmiarX()} {self.swiat.getRozmiarY()} {self.swiat.getNumerTury()} ")
        f.write(f"{len(self.swiat.getOrganizmy())} {self.swiat.getCooldown()} \n")

        self.swiat.sortujOrganizmy()

        for o in self.swiat.getOrganizmy():
            f.write(f"{o.generujKomende()} \n")

        f.write("#ZAPIS GRY WIRTUALNY SWIAT v3.0#\n")
        f.write("#Damian Jankowski s188597#\n")
        f.write("#znak polX polY sila inicjatywa wiek#\n")
        f.write("#[A]ntylopa [C]zlowiek [S]uperman [L]is [O]wca [W]ilk [Z]olw#\n")
        f.write("#[B]arszcz [G]uarana [M]lecz [T]rawa [X]Wilczejagody [R]CyberOwca#\n")
        f.write("#Superman - czlowiek z wlaczona umiejetnoscia#\n")
        f.close()

    def wczytajGre(self, nazwapliku):
        f = open(nazwapliku, "r")

        tab = f.readline().rstrip().split(" ")

        self.swiat = Swiat(int(tab[0]), int(tab[1]))
        self.swiat.setNumerTury(int(tab[2]))
        self.swiat.setCooldown(int(tab[4]))

        for i in range(int(tab[3])):
            org = f.readline().rstrip().split(" ")
            self.swiat.dodajOrganizmMod(org[0], Punkt(int(org[1]), int(org[2])), int(org[3]), int(org[4]), int(org[5]))
        f.close()
        self.swiat.wyczyscDziennik()
        return self.swiat

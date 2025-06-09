import random

from PyQt5.QtCore import Qt

from Punkt import Punkt
from Zwierzeta.Zwierze import Zwierze


class Czlowiek(Zwierze):

    def __init__(self, miejsce, swiat):
        super(Czlowiek, self).__init__("Człowiek", miejsce, 5, 4, "C", "red", swiat)

    def stworzdziecko(self, p):
        pass

    def akcja(self):
        x, y = self.lokacja.getX(), self.lokacja.getY()
        wybrany = self.swiat.getWybrany()
        cooldown = self.swiat.getCooldown()
        mnoznik = 1

        if wybrany == Qt.Key_Q and cooldown == 0:
            cooldown = 11
            self.kolor = "gold"
            self.znak = "S"
        if cooldown > 5:
            mnoznik = 2
        if 9 > cooldown > 6:
            mnoznik = random.randint(1, 2)
        elif cooldown == 6:
            self.znak = "C"
            self.kolor = "red"
            mnoznik = 1
        if cooldown:
            cooldown -= 1

        self.swiat.setCooldown(cooldown)
        if wybrany == Qt.Key_Up:
            if y > -1 + mnoznik:
                y -= mnoznik
        elif wybrany == Qt.Key_Down:
            if y < self.swiat.getRozmiarY() - mnoznik:
                y += mnoznik
        elif wybrany == Qt.Key_Right:
            if x < self.swiat.getRozmiarX() - mnoznik:
                x += mnoznik
        elif wybrany == Qt.Key_Left:
            if x > -1 + mnoznik:
                x -= mnoznik
        else:
            self.swiat.dodajWpis(f"{self} nie poruszył się")
            return
        cel = Punkt(x, y)
        self.swiat.dodajWpisAkcja(self, cel)
        self.kolizja(cel)

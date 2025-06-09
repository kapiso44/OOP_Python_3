import math

from Punkt import Punkt
from Zwierzeta.Zwierze import Zwierze


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


class CyberOwca(Zwierze):

    def __init__(self, miejsce, swiat):
        super(CyberOwca, self).__init__("Cyber Owca", miejsce, 11, 4, "R", "brown", swiat)

    def stworzdziecko(self, p):
        return CyberOwca(p, self.swiat)

    def akcja(self):
        wrog = self.znajdzNajblizszyBarszcz()

        if wrog is not None:
            self.swiat.dodajWpis(f"{self} wykrył {self.swiat.getPolePlanszy(wrog)}")
            cel = Punkt(self.getLokacja().getX() + sign(wrog.getX() - self.getLokacja().getX()),
                        self.getLokacja().getY() + sign(wrog.getY() - self.getLokacja().getY()))
        else:
            cel = self.losujRuch(self.lokacja, 1)

        self.kolizja(cel)

    def znajdzNajblizszyBarszcz(self):
        odl = math.inf
        cel = None
        for org in self.swiat.getOrganizmy():
            from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
            if isinstance(org, BarszczSosnowskiego):
                dystans = self.getOdleglosc(org.getLokacja())
                if odl > dystans:
                    odl = dystans
                    cel = org.getLokacja()

        return cel

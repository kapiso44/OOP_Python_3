from Punkt import Punkt
from Rosliny.Roslina import Roslina
from Zwierzeta.CyberOwca import CyberOwca
from Zwierzeta.Zwierze import Zwierze


class BarszczSosnowskiego(Roslina):

    def __init__(self, miejsce, swiat):
        super(BarszczSosnowskiego, self).__init__("Barszcz Sosnowskiego", miejsce, 10, 0, "B", "lightseagreen", swiat)

    def stworzdziecko(self, p):
        return BarszczSosnowskiego(p, self.swiat)

    def akcja(self):
        kier = self.swiat.getKierunki()

        for i in range(len(kier) - 1):
            miejsce = Punkt(self.lokacja.getX() + kier[i][0], self.lokacja.getY() + kier[i][1])
            if self.swiat.sprawdzGranice(miejsce):
                obok = self.swiat.getPolePlanszy(miejsce)
                if isinstance(obok, Zwierze) and isinstance(obok, CyberOwca) is False:
                    self.swiat.dodajWpis(f"{self} zabił {obok}")
                    obok.setZyje(False)
                    self.swiat.setPolePlanszy(obok.getLokacja(), None)
        super(BarszczSosnowskiego, self).akcja()

    def czyZjadlSpecjalna(self, jedzacy):
        self.zyje = False
        self.swiat.setPolePlanszy(self.lokacja, None)
        return True

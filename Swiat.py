from Punkt import Punkt
from Rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from Rosliny.Guarana import Guarana
from Rosliny.Mlecz import Mlecz
from Rosliny.Trawa import Trawa
from Rosliny.WilczeJagody import WilczeJagody
from Zwierzeta.Antylopa import Antylopa
from Zwierzeta.CyberOwca import CyberOwca
from Zwierzeta.Czlowiek import Czlowiek
from Zwierzeta.Lis import Lis
from Zwierzeta.Owca import Owca
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Zolw import Zolw


class Swiat:
    dziennik = []
    organizmy = []
    wybrany = 0
    plansza = None
    czyZyjeCzlowiek = False
    numerTury = 0
    cooldown = 0
    rozmiarX = 0
    rozmiarY = 0

    def __init__(self, _szer, _wys):
        self.rozmiarX = _szer
        self.rozmiarY = _wys
        self.plansza = [[None for x in range(_szer)] for y in range(_wys)]
        self.dziennik = []
        self.organizmy = []

    def getKierunki(self):
        return [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    def getWybrany(self):
        return self.wybrany

    def setWybrany(self, x):
        self.wybrany = x

    def getPolePlanszy(self, p):
        return self.plansza[p.getY()][p.getX()]

    def setPolePlanszy(self, p, o):
        self.plansza[p.getY()][p.getX()] = o

    def wyczyscDziennik(self):
        self.dziennik.clear()

    def getOrganizmy(self):
        return self.organizmy

    def getNumerTury(self):
        return self.numerTury

    def setNumerTury(self, numerTury):
        self.numerTury = numerTury

    def getRozmiarX(self):
        return self.rozmiarX

    def getRozmiarY(self):
        return self.rozmiarY

    def getCzyZyjeCzlowiek(self):
        return self.czyZyjeCzlowiek

    def getCooldown(self):
        return self.cooldown

    def setCooldown(self, cooldown):
        self.cooldown = cooldown

    def dodajWpis(self, wiad):
        self.dziennik.append(wiad)

    def dodajWpisAkcja(self, o, p):
        self.dziennik.append(f"{o} chce iść {p}")

    def sprawdzGranice(self, p):
        return self.rozmiarX > p.getX() >= 0 and self.rozmiarY > p.getY() >= 0

    def sprawdzMiejsce(self, p):
        for i in range(len(self.getKierunki()) - 1):
            miejsce = Punkt(p.getX() + self.getKierunki()[i][0], p.getY() + self.getKierunki()[i][1])
            if self.sprawdzGranice(miejsce):
                if self.getPolePlanszy(miejsce) is None:
                    return miejsce
        self.dodajWpis(f"Wokół {p} nie ma miejsca")
        return None

    def dodajOrganizm(self, nowy):
        miejsce = nowy.getLokacja()
        if self.sprawdzGranice(miejsce):
            if self.getPolePlanszy(miejsce) is None:
                if isinstance(nowy, Czlowiek):
                    self.czyZyjeCzlowiek = True
                self.organizmy.append(nowy)
                self.setPolePlanszy(miejsce, nowy)
            else:
                self.dodajWpis(f"<span style=\"color:red\">Błąd zapisu! Miejsce {miejsce} zajęte</span>")
        else:
            self.dodajWpis(f"<span style=\"color:red\">Błąd zapisu! Miejsce {miejsce} nie istnieje</span>")

    def dodajOrganizmMod(self, _znak, miejsce, sila, inicjatywa, wiek):
        nowy = None
        znak = _znak[0]
        if znak == "W":
            nowy = Wilk(miejsce, self)
        if znak == "O":
            nowy = Owca(miejsce, self)
        if znak == "L":
            nowy = Lis(miejsce, self)
        if znak == "Z":
            nowy = Zolw(miejsce, self)
        if znak == "A":
            nowy = Antylopa(miejsce, self)
        if znak == "R":
            nowy = CyberOwca(miejsce, self)
        if znak == "C":
            nowy = Czlowiek(miejsce, self)
        if znak == "S":
            nowy = Czlowiek(miejsce, self)
            nowy.setZnak("S")
            nowy.setKolor("gold")
        if znak == "T":
            nowy = Trawa(miejsce, self)
        if znak == "M":
            nowy = Mlecz(miejsce, self)
        if znak == "G":
            nowy = Guarana(miejsce, self)
        if znak == "X":
            nowy = WilczeJagody(miejsce, self)
        if znak == "B":
            nowy = BarszczSosnowskiego(miejsce, self)

        if isinstance(nowy, Czlowiek) and self.czyZyjeCzlowiek:
            self.dodajWpis("<span style=\"color:red\">Błąd! Człowiek już istnieje</span>")
            return

        if nowy is not None:
            self.dodajOrganizm(nowy)
            self.dodajWpis(f"<span style=\"color:red\">Dodano {nowy}</span>")
            if (sila and inicjatywa and wiek) != -1:
                nowy.setSila(sila)
                nowy.setInicjatywa(inicjatywa)
                nowy.setWiek(wiek)

    def sortujOrganizmy(self):
        self.organizmy.sort(key=lambda org: (org.getInicjatywa(), org.getWiek()), reverse=True)

    def usunMartwe(self):
        for martwy in self.organizmy:
            if martwy.getZyje() is False:
                if isinstance(martwy, Czlowiek):
                    self.czyZyjeCzlowiek = False
                self.organizmy.remove(martwy)

    def wykonajTure(self):
        self.sortujOrganizmy()
        for o in self.organizmy:
            if o.getNarodzony():
                o.setNarodzony(False)

        for o in self.organizmy:
            if o.getNarodzony() is False and o.getZyje() is True:
                o.akcja()
                o.setWiek(o.getWiek() + 1)
                self.dodajWpis("----")

        self.usunMartwe()
        self.numerTury += 1

    def drukujCooldown(self):
        info = ""
        if self.czyZyjeCzlowiek:
            info += "<span style=\"color:red; font-size:15px\">Człowiek żyje! Poruszaj się strzałkami.</span><br/>"
            if self.cooldown > 5:
                info += f"<span style=\"color:red; font-size:15px\">Umiejętność Szybkość antylopy aktywna jeszcze " \
                        f"przez {self.cooldown - 5} tur</span><br/>"
            if 8 > self.cooldown > 5:
                info += "<span style=\"color:red; font-size:15px\">Prawdopodobieństwo 50%</span><br/>"
            if 6 > self.cooldown > 0:
                info += f"<span style=\"color:red; font-size:15px\">Nie możesz użyć umiejętności jeszcze przez " \
                        f"{self.cooldown} tur</span><br/>"
        return info

    def drukujDziennik(self):
        zapis = f"<h3>Dziennik:</h3>Na świecie jest <span style=\"font-size:25px\"> {len(self.organizmy)}</span> " \
                f"organizmów. Tura nr <span style=\"font-size:25px\">{self.numerTury} </span><br/>"
        i, j = 0, 0
        for o in self.organizmy:
            i += 1
            if i > 10:
                break
            zapis += o.info()
            zapis += "<br/>"

        zapis += "<hr>"
        for wiad in self.dziennik:
            j += 1
            if j > 30:
                break
            zapis += wiad
            zapis += "<br/>"
        return zapis

    def utworz_organizm_z_danych(self, dane):
        """Helper used during loading to recreate an organism."""
        if isinstance(dane, str):
            dane = dane.strip().split(" ")
        if len(dane) < 6:
            return
        znak, x, y, sila, inicjatywa, wiek = dane[:6]
        self.dodajOrganizmMod(
            znak,
            Punkt(int(x), int(y)),
            int(sila),
            int(inicjatywa),
            int(wiek),
        )

    def zapisz_stan(self, nazwapliku):
        """Zapisz stan świata do pliku."""
        with open(nazwapliku, "w") as f:
            f.write(
                f"{self.rozmiarX} {self.rozmiarY} {self.numerTury} {len(self.organizmy)} {self.cooldown}\n"
            )
            self.sortujOrganizmy()
            for o in self.organizmy:
                f.write(f"{o.generujKomende()} \n")

            f.write("#ZAPIS GRY WIRTUALNY SWIAT v3.0#\n")
            f.write("#Damian Jankowski s188597#\n")
            f.write("#znak polX polY sila inicjatywa wiek#\n")
            f.write("#[A]ntylopa [C]zlowiek [S]uperman [L]is [O]wca [W]ilk [Z]olw#\n")
            f.write(
                "#[B]arszcz [G]uarana [M]lecz [T]rawa [X]Wilczejagody [R]CyberOwca#\n"
            )
            f.write("#Superman - czlowiek z wlaczona umiejetnoscia#\n")

    @classmethod
    def wczytaj_stan(cls, nazwapliku):
        """Wczytaj stan świata z pliku i zwróć nową instancję."""
        with open(nazwapliku, "r") as f:
            tab = f.readline().rstrip().split(" ")

            swiat = cls(int(tab[0]), int(tab[1]))
            swiat.setNumerTury(int(tab[2]))
            swiat.setCooldown(int(tab[4]))

            for _ in range(int(tab[3])):
                org = f.readline().rstrip().split(" ")
                swiat.utworz_organizm_z_danych(org)

        swiat.wyczyscDziennik()
        return swiat

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

    # New helper API used by the console implementation
    def dodaj_komunikat(self, wiadomosc: str):
        """Alias for dodajWpis for compatibility with early versions."""
        self.dodajWpis(wiadomosc)

    def czy_pole_w_granicach(self, x: int, y: int) -> bool:
        """Sprawdza czy wskazane pole znajduje się na planszy."""
        return 0 <= x < self.rozmiarX and 0 <= y < self.rozmiarY

    def dodaj_organizm(self, organizm):
        """Dodaje organizm do świata (skrót kompatybilności)."""
        self.dodajOrganizm(organizm)

    def usun_organizm(self, organizm):
        """Usuwa organizm z listy i planszy, jeśli jest obecny."""
        if organizm in self.organizmy:
            self.organizmy.remove(organizm)
        p = organizm.getLokacja()
        if self.czy_pole_w_granicach(p.getX(), p.getY()):
            if self.getPolePlanszy(p) is organizm:
                self.setPolePlanszy(p, None)
        if isinstance(organizm, Czlowiek):
            self.czyZyjeCzlowiek = False

    def przesun_organizm(self, organizm, nowy_x: int, nowy_y: int):
        """Przesuwa organizm na nowe pole z obsługą kolizji."""
        if not self.czy_pole_w_granicach(nowy_x, nowy_y):
            return False

        stary_x, stary_y = organizm.getLokacja().getX(), organizm.getLokacja().getY()
        cel = self.plansza[nowy_y][nowy_x]

        if cel is not None and cel is not organizm:
            # Kolizja - logikę obsługuje metoda kolizja organizmu
            organizm.kolizja(Punkt(nowy_x, nowy_y))
        else:
            # Wolne pole - zwykłe przesunięcie
            self.plansza[stary_y][stary_x] = None
            self.plansza[nowy_y][nowy_x] = organizm
            organizm.lokacja = Punkt(nowy_x, nowy_y)

        return True

    def rysuj_plansze(self) -> str:
        """Zwraca tekstową reprezentację planszy wraz z dziennikiem."""
        linie = ["+" + "-" * self.rozmiarX + "+"]
        for y in range(self.rozmiarY):
            wiersz = "|"
            for x in range(self.rozmiarX):
                org = self.plansza[y][x]
                wiersz += org.getZnak() if org else " "
            linie.append(wiersz + "|")
        linie.append("+" + "-" * self.rozmiarX + "+")
        if self.dziennik:
            linie.append("\nZdarzenia:")
            for msg in self.dziennik:
                linie.append(f"- {msg}")
        return "\n".join(linie)

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

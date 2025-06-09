import math
import random
from abc import ABC, abstractmethod

from Punkt import Punkt


class Organizm(ABC):
    nazwa = "Organizm"
    swiat = None
    sila = 0
    inicjatywa = 0
    wiek = 0
    lokacja = None
    znak = "?"
    zyje = True
    narodzony = False
    kolor = 0

    def __init__(self, nazwa, miejsce, sila, inicjatywa, znak, kolor, swiat):
        self.nazwa = nazwa
        self.lokacja = miejsce
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.swiat = swiat
        self.znak = znak
        self.kolor = kolor

    def __str__(self):
        return f"{self.nazwa} {self.lokacja}"

    def info(self):
        return f"{self.nazwa} {self.lokacja} Siła: {self.sila} Inicjatywa: " \
               f"{self.inicjatywa} Wiek: {self.wiek}"

    def generujKomende(self):
        return f"{self.znak} {self.lokacja.getX()} {self.lokacja.getY()} " \
               f"{self.sila} {self.inicjatywa} {self.wiek}"

    def czyOdbilAtak(self, atakujacy):
        return False

    def czyUniknalAtak(self, atakujacy):
        return False

    def czyZjadlSpecjalna(self, jedzacy):
        return False

    @abstractmethod
    def stworzdziecko(self, p):
        pass

    def getOdleglosc(self, a):
        return math.sqrt(pow(a.getX() - self.lokacja.getX(), 2) + pow(a.getY() - self.lokacja.getY(), 2))

    def losujRuch(self, p, zasieg):
        kier = self.swiat.getKierunki()
        mnoznik = random.randint(1, zasieg)
        i = random.randint(0, len(kier) - 1)
        temp = Punkt(p.getX() + mnoznik * kier[i][0], p.getY() + mnoznik * kier[i][1])
        if self.swiat.sprawdzGranice(temp) is True:
            return temp
        else:
            return p

    def kolizja(self, miejsce):
        atakowany = self.swiat.getPolePlanszy(miejsce)

        if atakowany is not None and atakowany is not self:
            if atakowany.getNazwa() is self.nazwa:
                self.swiat.dodajWpis(f"{self} próbuje urodzić")
                if random.randint(0, 3) > 0:
                    self.swiat.dodajWpis(f"{self} poronił")
                    return
                p = self.swiat.sprawdzMiejsce(miejsce)
                if p is not None:
                    dziecko = self.stworzdziecko(p)
                    dziecko.setNarodzony(True)
                    self.swiat.dodajOrganizm(dziecko)
                    self.swiat.dodajWpis(f"{self} rozmnożył się")
            elif self.zyje is True and atakowany.getZyje() is True:
                self.atakowanie(atakowany)
        elif atakowany is self:
            self.swiat.dodajWpis(f"{self} nie poruszył się")
        else:
            self.swiat.dodajWpis(f"{self} sukces!")
            self.swiat.setPolePlanszy(self.lokacja, None)
            self.lokacja = miejsce
            self.swiat.setPolePlanszy(self.lokacja, self)

    def atakowanie(self, atakowany):
        from Rosliny.Roslina import Roslina
        if isinstance(atakowany, Roslina):
            atakowany.kolizja(self)
            if self.getZyje() and atakowany.getZyje() is False:
                self.swiat.setPolePlanszy(self.lokacja, None)
                self.lokacja = atakowany.getLokacja()
                self.swiat.setPolePlanszy(self.lokacja, self)
            return

        if atakowany.czyOdbilAtak(self):
            self.swiat.dodajWpis(f"{atakowany} odbił atak od {self}")
        elif atakowany.czyUniknalAtak(self):
            self.swiat.dodajWpis(f"{atakowany} uniknął ataku od {self}")
        elif atakowany.getSila() >= self.sila:
            if atakowany.czyZjadlSpecjalna(self):
                self.swiat.dodajWpis(f"{self} doznał efektu od {atakowany}")
            self.swiat.dodajWpis(f"{atakowany} zabił {self}")
            self.zyje = False
            self.swiat.setPolePlanszy(self.lokacja, None)
        else:
            if atakowany.czyZjadlSpecjalna(self):
                self.swiat.dodajWpis(f"{self} doznał efektu od {atakowany}")
            if isinstance(atakowany, Roslina):
                self.swiat.dodajWpis(f"{self} zjadł {atakowany}")
            else:
                self.swiat.dodajWpis(f"{self} zabił {atakowany}")
            atakowany.setZyje(False)
            self.swiat.setPolePlanszy(atakowany.getLokacja(), self)
            self.swiat.setPolePlanszy(self.lokacja, None)
            self.lokacja = atakowany.getLokacja()

    def getZyje(self):
        return self.zyje

    def setZyje(self, zyje):
        self.zyje = zyje

    def rysowanie(self):
        return self.kolor

    def getWiek(self):
        return self.wiek

    def setWiek(self, wiek):
        self.wiek = wiek

    def getInicjatywa(self):
        return self.inicjatywa

    def setInicjatywa(self, inicjatywa):
        self.inicjatywa = inicjatywa

    def getSila(self):
        return self.sila

    def setSila(self, sila):
        self.sila = sila

    def getNarodzony(self):
        return self.narodzony

    def setNarodzony(self, narodzony):
        self.narodzony = narodzony

    def getNazwa(self):
        return self.nazwa

    def getLokacja(self):
        return self.lokacja

    def setKolor(self, kolor):
        self.kolor = kolor

    def getZnak(self):
        return self.znak

    def setZnak(self, znak):
        self.znak = znak

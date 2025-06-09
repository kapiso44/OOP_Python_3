from MenedzerSave import MenedzerSave
from Punkt import Punkt

class Console:
    KEY_MAP = {
        'w': 16777235,  # up
        's': 16777237,  # down
        'a': 16777234,  # left
        'd': 16777236,  # right
        'u': 81         # specjalna umiejetnosc
    }

    def __init__(self):
        self.swiat = None

    def _instructions(self):
        print("\n=== STEROWANIE ===")
        print("w/a/s/d - ruch czlowieka")
        print("u - specjalna umiejetnosc")
        print("n - nastepna tura")
        print("z - zapisz gre")
        print("o - wczytaj gre")
        print("q - wyjdz")

    def _rysuj_swiat(self):
        if self.swiat is None:
            return
        print(f"\n=== TURA {self.swiat.getNumerTury()} ===")
        print("+" + "-" * self.swiat.getRozmiarX() + "+")
        for y in range(self.swiat.getRozmiarY()):
            linia = "|"
            for x in range(self.swiat.getRozmiarX()):
                o = self.swiat.getPolePlanszy(Punkt(x, y))
                linia += o.getZnak() if o else " "
            linia += "|"
            print(linia)
        print("+" + "-" * self.swiat.getRozmiarX() + "+")
        print(self.swiat.drukujCooldown())
        print(self.swiat.drukujDziennik())
        self.swiat.wyczyscDziennik()

    def _wykonaj_ture(self, key=0):
        if self.swiat is None:
            return
        self.swiat.setWybrany(key)
        self.swiat.wykonajTure()

    def nowa_gra(self, szer, wys, gestosc):
        ilosc = int(szer * wys * gestosc / 100)
        self.swiat = MenedzerSave(None).generujGre(szer, wys, ilosc)

    def zapisz_gre(self, plik):
        if self.swiat:
            MenedzerSave(self.swiat).zapiszGre(plik)

    def wczytaj_gre(self, plik):
        self.swiat = MenedzerSave(None).wczytajGre(plik)

    def run(self):
        while True:
            if self.swiat is None:
                print("1. Nowa gra")
                print("2. Wczytaj gre")
                print("3. Wyjscie")
                opcja = input("Wybierz: ")
                if opcja == '1':
                    x = int(input("Szerokosc: "))
                    y = int(input("Wysokosc: "))
                    z = int(input("Zageszczenie (%): "))
                    self.nowa_gra(x, y, z)
                    self._rysuj_swiat()
                    self._instructions()
                elif opcja == '2':
                    nazwa = input("Plik: ")
                    self.wczytaj_gre(nazwa)
                    self._rysuj_swiat()
                    self._instructions()
                else:
                    break
            else:
                cmd = input("> ").lower()
                if cmd == 'q':
                    break
                elif cmd == 'z':
                    self.zapisz_gre(input("Nazwa pliku: "))
                elif cmd == 'o':
                    self.wczytaj_gre(input("Nazwa pliku: "))
                    self._rysuj_swiat()
                    self._instructions()
                elif cmd == 'n':
                    self._wykonaj_ture()
                    self._rysuj_swiat()
                else:
                    key = self.KEY_MAP.get(cmd)
                    if key is not None:
                        self._wykonaj_ture(key)
                        self._rysuj_swiat()
        print("Koniec gry")

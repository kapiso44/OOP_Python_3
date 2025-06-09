class Swiat:
    def __init__(self, szerokosc: int = 20, wysokosc: int = 20):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.organizmy: List[Organizm] = []
        self.plansza = [[None for _ in range(szerokosc)] for _ in range(wysokosc)]
        self.komunikaty: List[str] = []
        self.tura = 0

    def wykonaj_ture(self):
        """Wykonuje jedną turę gry"""
        self.tura += 1
        self.komunikaty.clear()

        # Sortowanie organizmów według inicjatywy, potem wieku
        self.organizmy.sort(key=lambda org: (-org.inicjatywa, -org.wiek))

        # Wykonanie akcji wszystkich organizmów
        organizmy_do_akcji = self.organizmy.copy()
        for organizm in organizmy_do_akcji:
            if organizm.zywy and organizm in self.organizmy:
                organizm.akcja()
                organizm.wiek += 1

    def przesun_organizm(self, organizm: Organizm, nowy_x: int, nowy_y: int):
        """Przesuwa organizm na nowe pole z obsługą kolizji"""
        if not self.czy_pole_w_granicach(nowy_x, nowy_y):
            return False

        stary_x, stary_y = organizm.x, organizm.y
        cel = self.plansza[nowy_y][nowy_x]

        if cel is not None:
            # Kolizja - wykonanie walki/interakcji
            if cel.kolizja(organizm):
                # Cel został pokonany/zjedzony
                self.plansza[stary_x][stary_y] = None
                self.plansza[nowy_x][nowy_y] = organizm
                organizm.x, organizm.y = nowy_x, nowy_y
        else:
            # Wolne pole - zwykłe przesunięcie
            self.plansza[stary_y][stary_x] = None
            self.plansza[nowy_y][nowy_x] = organizm
            organizm.x, organizm.y = nowy_x, nowy_y

        return True

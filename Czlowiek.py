class Czlowiek(Zwierze):
    def __init__(self, x: int, y: int, swiat, numer_indeksu: int):
        super().__init__(x, y, swiat, sila=5, inicjatywa=4)
        self.kierunek_ruchu = None
        self.umiejetnosc_id = numer_indeksu % 5
        self.umiejetnosc_aktywna = False
        self.czas_dzialania_umiejetnosci = 0
        self.cooldown_umiejetnosci = 0

    def ustaw_kierunek(self, kierunek: str):
        """Ustawia kierunek ruchu na podstawie wciśniętego klawisza"""
        self.kierunek_ruchu = kierunek

    def akcja(self):
        """Człowiek porusza się według kierunku gracza"""
        if not self.zywy or self.kierunek_ruchu is None:
            return

        dx, dy = self.pobierz_przemieszczenie(self.kierunek_ruchu)
        nowy_x, nowy_y = self.x + dx, self.y + dy

        if self.swiat.czy_pole_w_granicach(nowy_x, nowy_y):
            self.swiat.przesun_organizm(self, nowy_x, nowy_y)

        self.kierunek_ruchu = None  # Reset kierunku

    def aktywuj_umiejetnosc(self):
        """Aktywuje specjalną umiejętność na 5 tur"""
        if self.cooldown_umiejetnosci == 0:
            self.umiejetnosc_aktywna = True
            self.czas_dzialania_umiejetnosci = 5
            self.cooldown_umiejetnosci = 10  # 5 tur działania + 5 tur przerwy

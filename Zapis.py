import json
import copy


def zapisz_stan(self, nazwa_pliku: str):
    """Zapisuje stan świata do pliku JSON"""
    stan = {
        'tura': self.tura,
        'szerokosc': self.szerokosc,
        'wysokosc': self.wysokosc,
        'organizmy': []
    }

    for organizm in self.organizmy:
        dane_organizmu = {
            'typ': type(organizm).__name__,
            'x': organizm.x,
            'y': organizm.y,
            'sila': organizm.sila,
            'inicjatywa': organizm.inicjatywa,
            'wiek': organizm.wiek,
            'zywy': organizm.zywy
        }
        stan['organizmy'].append(dane_organizmu)

    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        json.dump(stan, plik, indent=2, ensure_ascii=False)


def wczytaj_stan(self, nazwa_pliku: str):
    """Wczytuje stan świata z pliku JSON"""
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        stan = json.load(plik)

    self.tura = stan['tura']
    self.szerokosc = stan['szerokosc']
    self.wysokosc = stan['wysokosc']

    # Rekonstrukcja planszy
    self.organizmy.clear()
    self.plansza = [[None for _ in range(self.szerokosc)]
                    for _ in range(self.wysokosc)]

    for dane in stan['organizmy']:
        organizm = self.utworz_organizm_z_danych(dane)
        self.dodaj_organizm(organizm)

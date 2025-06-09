def rysuj_swiat(self):
    """Wyświetla stan świata w konsoli"""
    print(f"\n=== TURA {self.tura} ===")
    print("+" + "-" * self.szerokosc + "+")

    for y in range(self.wysokosc):
        linia = "|"
        for x in range(self.szerokosc):
            organizm = self.plansza[y][x]
            if organizm is not None:
                linia += organizm.rysowanie()
            else:
                linia += " "
        linia += "|"
        print(linia)

    print("+" + "-" * self.szerokosc + "+")

    # Wyświetlanie komunikatów z tury
    if self.komunikaty:
        print("\nWydarzenia w tej turze:")
        for komunikat in self.komunikaty:
            print(f"- {komunikat}")


def wyswietl_instrukcje(self):
    """Wyświetla instrukcje sterowania"""
    print("\n=== STEROWANIE ===")
    print("Strzałki - ruch człowieka")
    print("SPACJA - następna tura")
    print("S - zapisz grę")
    print("L - wczytaj grę")
    print("Q - wyjście")

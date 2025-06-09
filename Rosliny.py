class Guarana(Roslina):
    def __init__(self, x: int, y: int, swiat):
        super().__init__(x, y, swiat, sila=0)

    def kolizja(self, agresor):
        """Zwiększa siłę zwierzęcia o 3"""
        if isinstance(agresor, Zwierze):
            agresor.sila += 3
            self.swiat.dodaj_komunikat(f"{type(agresor).__name__} zjadł guaranę i zwiększył siłę do {agresor.sila}")
        super().kolizja(agresor)
        return True


class WilczeJagody(Roslina):
    def __init__(self, x: int, y: int, swiat):
        super().__init__(x, y, swiat, sila=99)

    def kolizja(self, agresor):
        """Zwierzę które zjadło tę roślinę ginie"""
        self.swiat.dodaj_komunikat(f"{type(agresor).__name__} zjadł wilcze jagody i umarł!")
        self.swiat.usun_organizm(agresor)
        super().kolizja(agresor)
        return True

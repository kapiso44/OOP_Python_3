from Rosliny.Roslina import Roslina


class Guarana(Roslina):

    def __init__(self, miejsce, swiat):
        super(Guarana, self).__init__("Guarana", miejsce, 0, 0, "G", "royalblue", swiat)

    def stworzdziecko(self, p):
        return Guarana(p, self.swiat)

    def czyZjadlSpecjalna(self, jedzacy):
        jedzacy.setSila(jedzacy.getSila() + 3)
        return True

    def kolizja(self, atakujacy):
        super(Guarana, self).kolizja(atakujacy)

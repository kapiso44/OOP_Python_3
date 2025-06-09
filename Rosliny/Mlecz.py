from Rosliny.Roslina import Roslina


class Mlecz(Roslina):

    def __init__(self, miejsce, swiat):
        super(Mlecz, self).__init__("Mlecz", miejsce, 0, 0, "M", "#e0e000", swiat)

    def stworzdziecko(self, p):
        return Mlecz(p, self.swiat)

    def akcja(self):
        for x in range(3):
            super(Mlecz, self).akcja()

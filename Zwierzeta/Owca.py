from Zwierzeta.Zwierze import Zwierze


class Owca(Zwierze):

    def __init__(self, miejsce, swiat):
        super(Owca, self).__init__("Owca", miejsce, 4, 4, "O", "gray", swiat)

    def stworzdziecko(self, p):
        return Owca(p, self.swiat)

from PyQt5.QtWidgets import QPushButton

from Punkt import Punkt


class PrzyciskKrata(QPushButton):

    def __init__(self, x, y, swiat, gui):
        super().__init__()
        miejsce = swiat.getPolePlanszy(Punkt(x, y))
        self.setMinimumSize(int((gui.szerOkna - 50) / swiat.getRozmiarX()),
                            int((gui.wysOkna / 2 - 50) / swiat.getRozmiarY()))
        self.setToolTip(f"({x},{y})")
        if miejsce is not None:
            pass
            self.setText(miejsce.getZnak())
            rozmiar = int(
                min(gui.szerOkna / swiat.getRozmiarX() - 7,
                    gui.wysOkna / (2 * swiat.getRozmiarY()) - 7))
            self.setStyleSheet(
                "QPushButton {font-size: " + str(
                    rozmiar) + "px ; color: white ; background-color : " + miejsce.rysowanie() + "}")
            self.setEnabled(False)
        else:
            self.clicked.connect(lambda state, finalX=x, finalY=y: gui.wyborOrganizmu(finalX, finalY))

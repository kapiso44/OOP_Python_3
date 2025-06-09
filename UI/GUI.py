import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QApplication, QLabel, \
    QMainWindow, QWidget, QDesktopWidget, QAction, QMenuBar, QScrollArea, QInputDialog, QFileDialog

from MenedzerSave import MenedzerSave
from Punkt import Punkt
from UI.NowaGraDialog import NowaGraDialog
from UI.PrzyciskKrata import PrzyciskKrata


class GUI(QMainWindow):
    glowna = None
    plansza = None
    scrollpanel = None
    logi = None

    menu = None

    nowagra = None
    nowaAkcja = None
    nowagraPopUp = None

    wczytaj = None
    wczytajAkcja = None
    wczytajPopUp = None

    zapisz = None
    zapiszAkcja = None
    zapiszPopUp = None

    wyjdz = None
    wyjdzAkcja = None

    layout = None
    kratalayout = None
    wyborOrganizmuPopUp = None

    szerOkna = 500
    wysOkna = 1000

    swiat = None

    def __init__(self):
        app = QApplication(sys.argv)
        super(GUI, self).__init__()
        self.setWindowTitle("Wirtualny Świat v3.0 Damian Jankowski s188597")
        self.setFixedSize(self.szerOkna, self.wysOkna)
        self.center()
        self.layout = QGridLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(self.layout)
        self.setCentralWidget(centralWidget)

        self.glowna = QtWidgets.QLabel()
        self.layout.addWidget(self.glowna)
        self.glowna.setText("<html><body style=\"text-align:center\"><h1>Gra Wirtualny Świat v3.0</h1>"
                            "<h2>Autor: Damian Jankowski s188597</h2>"
                            "<h3>Sterowanie:<br/>"
                            "Strzałki - poruszanie się człowiekiem<br/>"
                            "Naciśnięcie klawisza spowoduje wykonanie nowej tury"
                            "<br/>Q - specjalna umiejętność</h3>"
                            "</body></html>")

        self.genMenuBar(False)
        self.show()
        sys.exit(app.exec_())

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def genMenuBar(self, flag):
        self.menu = QMenuBar()
        self.nowaAkcja = QAction("Nowa gra")
        self.dodajPrzyciskMenu(self.nowaAkcja, self.nowaGraPopUp)
        if flag:
            self.zapiszAkcja = QAction("Zapisz grę")
            self.dodajPrzyciskMenu(self.zapiszAkcja, self.zapiszGre)
        self.wczytajAkcja = QAction("Wczytaj grę")
        self.dodajPrzyciskMenu(self.wczytajAkcja, self.wczytajGre)
        self.wyjdzAkcja = QAction("Wyjdź")
        self.dodajPrzyciskMenu(self.wyjdzAkcja, self.close)
        self.setMenuBar(self.menu)

    def dodajPrzyciskMenu(self, a, b):
        a.triggered.connect(b)
        self.menu.addAction(a)

    def odswiezEkran(self):
        if self.plansza is not None:
            self.layout.removeWidget(self.plansza)
            self.plansza.deleteLater()
        if self.scrollpanel is not None:
            self.layout.removeWidget(self.scrollpanel)
            self.scrollpanel.deleteLater()
        if self.glowna is not None:
            self.layout.removeWidget(self.glowna)
            self.glowna.deleteLater()
            self.glowna = None
        self.rysujSwiat()
        self.rysujDziennik()

    def keyPressEvent(self, e):
        if self.swiat is not None:
            if self.swiat.getCzyZyjeCzlowiek():
                self.swiat.setWybrany(e.key())
            self.swiat.wykonajTure()
            self.odswiezEkran()

    def nowaGraPopUp(self):
        dialog = NowaGraDialog()
        dialog.exec()
        if dialog.accepted is True:
            out = dialog.output
            zageszczenie = int(out[2] / 100 * out[0] * out[1])
            self.swiat = MenedzerSave(None).generujGre(out[0], out[1], zageszczenie)

        if self.swiat is not None:
            self.genMenuBar(True)
            self.odswiezEkran()

    def wczytajGre(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "Wczytaj grę", "",
                                                  "Plik zapisu (*.sv)", options=options)
        if filename:
            self.swiat = MenedzerSave(None).wczytajGre(filename)
            self.swiat.dodajWpis(f"<span style=\"color:red\">Wczytano grę z {filename}!</span>")
            self.genMenuBar(True)
            self.odswiezEkran()

    def zapiszGre(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.DontConfirmOverwrite
        filename, _ = QFileDialog.getSaveFileName(self, "Zapisz grę", "mojzapis.sv",
                                                  "Plik zapisu (*.sv)", options=options)
        if filename:
            MenedzerSave(self.swiat).zapiszGre(filename)
            self.swiat.dodajWpis(f"<span style=\"color:red\">Zapisano grę w {filename}!</span>")
            self.odswiezEkran()

    def rysujSwiat(self):
        if self.swiat is None:
            return
        self.plansza = QWidget()
        self.kratalayout = QGridLayout()
        self.plansza.setLayout(self.kratalayout)
        self.plansza.setMaximumSize(self.szerOkna - 20, int(self.wysOkna / 2) - 20)

        for y in range(self.swiat.getRozmiarY()):
            for x in range(self.swiat.getRozmiarX()):
                przycisk = PrzyciskKrata(x, y, self.swiat, self)
                self.kratalayout.addWidget(przycisk, y, x)

        self.layout.addWidget(self.plansza, 0, 0)

    def wyborOrganizmu(self, x, y):
        gatunki = ["W-Wilk", "L-Lis", "O-Owca", "Z-Żółw", "A-Antylopa", "C-Człowiek", "R-CyberOwca", "T-Trawa",
                   "M-Mlecz", "G-Guarana", "X-Wilcze Jagody", "B-Barszcz Sosnowskiego"]
        self.wyborOrganizmuPopUp, ok = QInputDialog.getItem(self, f"Dodawanie",
                                                            f"Wybierz gatunek na pole {x},{y}", gatunki, 0, False)
        if ok:
            self.swiat.dodajOrganizmMod(self.wyborOrganizmuPopUp[0], Punkt(x, y), -1, -1, -1)
            self.odswiezEkran()

    def rysujDziennik(self):
        if self.swiat is None:
            return
        self.scrollpanel = QScrollArea()
        self.logi = QLabel()
        self.logi.setText(f"<html> {self.swiat.drukujCooldown()} {self.swiat.drukujDziennik()} </html>")
        self.logi.setLayout(QGridLayout())
        self.logi.setAlignment(Qt.AlignTop)
        self.scrollpanel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollpanel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollpanel.setWidgetResizable(True)
        self.scrollpanel.setWidget(self.logi)
        self.layout.addWidget(self.scrollpanel, 1, 0)
        self.swiat.wyczyscDziennik()

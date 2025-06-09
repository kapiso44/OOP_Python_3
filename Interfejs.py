import tkinter as tk
from tkinter import messagebox, filedialog


class InterfejGraficzny:
    def __init__(self, swiat: Swiat):
        self.swiat = swiat
        self.root = tk.Tk()
        self.root.title("Symulator Wirtualnego Świata")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack()

        # Przyciski sterowania
        frame_kontroli = tk.Frame(self.root)
        frame_kontroli.pack()

        tk.Button(frame_kontroli, text="Następna tura",
                  command=self.nastepna_tura).pack(side=tk.LEFT)
        tk.Button(frame_kontroli, text="Zapisz",
                  command=self.zapisz_gre).pack(side=tk.LEFT)
        tk.Button(frame_kontroli, text="Wczytaj",
                  command=self.wczytaj_gre).pack(side=tk.LEFT)

    def rysuj_swiat(self):
        """Rysuje świat na canvas"""
        self.canvas.delete("all")
        rozmiar_pola = min(600 // self.swiat.szerokosc, 400 // self.swiat.wysokosc)

        for y in range(self.swiat.wysokosc):
            for x in range(self.swiat.szerokosc):
                x1, y1 = x * rozmiar_pola, y * rozmiar_pola
                x2, y2 = x1 + rozmiar_pola, y1 + rozmiar_pola

                organizm = self.swiat.plansza[y][x]
                if organizm:
                    kolor = self.pobierz_kolor_organizmu(organizm)
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=kolor, outline='black')
                    self.canvas.create_text(x1 + rozmiar_pola // 2,
                                            y1 + rozmiar_pola // 2,
                                            text=organizm.rysowanie())

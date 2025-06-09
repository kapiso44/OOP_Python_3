def pobierz_kolejnosc_organizmow(self):
    """Zwraca organizmy posortowane według kolejności działania"""
    return sorted(self.organizmy,
                 key=lambda org: (-org.inicjatywa, -org.wiek),
                 reverse=False)

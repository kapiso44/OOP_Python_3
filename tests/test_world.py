import pytest
from MenedzerSave import MenedzerSave
from Swiat import Swiat
from Punkt import Punkt
from Zwierzeta.Wilk import Wilk
from Zwierzeta.Owca import Owca


def test_generuj_swiat():
    mgr = MenedzerSave(None)
    swiat = mgr.generujGre(5, 5, 3)
    assert swiat.getRozmiarX() == 5
    assert swiat.getRozmiarY() == 5
    assert len(swiat.getOrganizmy()) == 3


def test_wilk_atakuje_owce():
    swiat = Swiat(3, 3)
    wilk = Wilk(Punkt(0, 0), swiat)
    owca = Owca(Punkt(1, 0), swiat)
    swiat.dodajOrganizm(wilk)
    swiat.dodajOrganizm(owca)

    wilk.kolizja(Punkt(1, 0))

    assert not owca.getZyje()
    assert wilk.getLokacja().getX() == 1
    assert wilk.getLokacja().getY() == 0
    assert swiat.getPolePlanszy(Punkt(1, 0)) is wilk

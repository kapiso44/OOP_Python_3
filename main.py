import argparse

from MenedzerSave import MenedzerSave
from Punkt import Punkt
from UI.GUI import GUI


QT_KEY_UP = 16777235
QT_KEY_DOWN = 16777237
QT_KEY_LEFT = 16777234
QT_KEY_RIGHT = 16777236
QT_KEY_Q = 81


def run_console(swiat):
    key_map = {
        'w': QT_KEY_UP,
        's': QT_KEY_DOWN,
        'a': QT_KEY_LEFT,
        'd': QT_KEY_RIGHT,
        'q': QT_KEY_Q,
    }
    while True:
        for y in range(swiat.getRozmiarY()):
            row = ''
            for x in range(swiat.getRozmiarX()):
                org = swiat.getPolePlanszy(Punkt(x, y))
                row += org.getZnak() if org else '.'
            print(row)
        for log in swiat.dziennik:
            print(log)
        swiat.wyczyscDziennik()
        cmd = input('w/a/s/d - ruch, q - umiej\u0119tno\u015b\u0107, x - wyj\u015bcie: ').strip().lower()
        if cmd == 'x':
            break
        swiat.setWybrany(key_map.get(cmd, 0))
        swiat.wykonajTure()


def main():
    parser = argparse.ArgumentParser(description='Gra Wirtualny \u015awi\u0105t')
    parser.add_argument('--mode', choices=['gui', 'console'], default='gui')
    parser.add_argument('--width', type=int, default=10)
    parser.add_argument('--height', type=int, default=10)
    parser.add_argument('--density', type=int, default=20, help='zageszczenie w %')
    args = parser.parse_args()

    mgr = MenedzerSave(None)
    amount = int(args.width * args.height * args.density / 100)
    swiat = mgr.generujGre(args.width, args.height, amount)

    if args.mode == 'gui':
        GUI(swiat)
    else:
        run_console(swiat)


if __name__ == '__main__':
    main()

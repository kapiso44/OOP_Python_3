import sys

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'console':
        from interfejs.console import Console
        Console().run()
    else:
        from UI.GUI import GUI
        GUI()


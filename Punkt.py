class Punkt:
    x = 0
    y = 0

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f"({self.x},{self.y})"

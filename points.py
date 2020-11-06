class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            x=self.x + other.x,
            y=self.y + other.y
        )

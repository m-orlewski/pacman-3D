import pyray as pr

CELL_WIDTH = 1.0
CELL_HEIGHT = 1.0
CELL_LENGTH = 1.0
POINT_RADIUS = 0.15
BOOST_RADIUS = 0.25

class Cell:
    def __init__(self, x, y, z):
        self.pos = pr.Vector3(x, y, z)


class Wall(Cell):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_cube(self.pos, CELL_WIDTH, CELL_HEIGHT, CELL_LENGTH, pr.GRAY)

class Point(Cell):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_sphere(self.pos, POINT_RADIUS, pr.GREEN)

class Boost(Cell):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_sphere(self.pos, BOOST_RADIUS, pr.RED)

class Tile(Cell):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pass
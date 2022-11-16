import pyray as pr

CELL_SIZE = 1.5
BOOST_RADIUS = 0.4
POINT_RADIUS = 0.2
class Cell:
    def __init__(self, x, y, z):
        self.pos = pr.Vector3(x, y, z)

class Wall(Cell):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_cube(self.pos, CELL_SIZE, CELL_SIZE/2, CELL_SIZE, pr.GRAY)

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
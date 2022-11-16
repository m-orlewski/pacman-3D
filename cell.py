import pyray as pr

CELL_SIZE = 1.5
BOOST_RADIUS = 0.4
POINT_RADIUS = 0.2
class Cell:
    def __init__(self, x, y, z):
        self.pos = pr.Vector3(x, y, z)

class Wall(Cell):
    '''Class for Wall tile'''

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_cube(self.pos, CELL_SIZE, CELL_SIZE/2, CELL_SIZE, pr.DARKBLUE)

class Point(Cell):
    '''Class for Point tile'''

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_sphere(self.pos, POINT_RADIUS, pr.Color(246, 190, 0, 255))

class Boost(Cell):
    '''Class for Boost tile'''

    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def draw(self):
        pr.draw_sphere(self.pos, BOOST_RADIUS, pr.RED)
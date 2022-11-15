import pyray as pr
import math

CELL_SIZE = 1.0
BOOST_RADIUS = 0.2
POINT_RADIUS = 0.1
class Cell:
    def __init__(self, i, j, mapWidth, mapHeight):
        self.i = i
        self.j = j
        self.pos = pr.Vector3(j - (math.floor(mapWidth/2)), 0, i - (math.floor(mapHeight/2)))
class Wall(Cell):
    def __init__(self, i, j, mapWidth, mapHeight):
        super().__init__(i, j, mapWidth, mapHeight)

    def draw(self):
        pr.draw_cube(self.pos, CELL_SIZE, CELL_SIZE, CELL_SIZE, pr.GRAY)

class Point(Cell):
    def __init__(self, i, j, mapWidth, mapHeight, collected=False):
        super().__init__(i, j, mapWidth, mapHeight)
        self.collected = collected

    def draw(self):
        if not self.collected:
            pr.draw_sphere(self.pos, POINT_RADIUS, pr.GREEN)

class Boost(Cell):
    def __init__(self, i, j, mapWidth, mapHeight, collected=False):
        super().__init__(i, j, mapWidth, mapHeight)
        self.collected = collected

    def draw(self):
        if not self.collected:
            pr.draw_sphere(self.pos, BOOST_RADIUS, pr.RED)
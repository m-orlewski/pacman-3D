import pyray as pr

from cell import Wall, Point, Boost, Tile

class Map():
    def __init__(self):
        self.map =[
            Wall(-5, 0, -5), Wall(-4, 0, -5), Wall(-3, 0, -5), Wall(-2, 0, -5), Wall(-1, 0, -5), Wall(0, 0, -5), Wall(1, 0, -5), Wall(2, 0, -5), Wall(3, 0, -5), Wall(4, 0, -5), Wall(5, 0, -5),
            Wall(-5, 0, -4), Boost(-4, 0, -4), Point(-3, 0, -4), Point(-2, 0, -4), Point(-1, 0, -4), Wall(0, 0, -4), Point(1, 0, -4), Point(2, 0, -4), Point(3, 0, -4), Point(4, 0, -4), Wall(5, 0, -4),
            Wall(-5, 0, -3), Point(-4, 0, -3), Wall(-3, 0, -3), Wall(-2, 0, -3), Point(-1, 0, -3), Wall(0, 0, -3), Point(1, 0, -3), Wall(2, 0, -3), Wall(3, 0, -3), Point(4, 0, -3), Wall(5, 0, -3),
            Wall(-5, 0, -2), Point(-4, 0, -2), Wall(-3, 0, -2), Point(-2, 0, -2), Point(-1, 0, -2), Point(0, 0, -2), Point(1, 0, -2), Point(2, 0, -2), Wall(3, 0, -2), Point(4, 0, -2), Wall(5, 0, -2),
            Wall(-5, 0, -1), Point(-4, 0, -1), Wall(-3, 0, -1), Point(-2, 0, -1), Wall(-1, 0, -1), Wall(0, 0, -1), Wall(1, 0, -1), Point(2, 0, -1), Wall(3, 0, -1), Point(4, 0, -1), Wall(5, 0, -1),
            Wall(-5, 0, 0), Point(-4, 0, 0), Point(-3, 0, 0), Point(-2, 0, 0), Point(-1, 0, 0), Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0), Point(4, 0, 0), Wall(5, 0, 0),
            Wall(-5, 0, 1), Point(-4, 0, 1), Wall(-3, 0, 1), Point(-2, 0, 1), Wall(-1, 0, 1), Wall(0, 0, 1), Wall(1, 0, 1), Point(2, 0, 1), Wall(3, 0, 1), Point(4, 0, 1), Wall(5, 0, 1),
            Wall(-5, 0, 2), Point(-4, 0, 2), Wall(-3, 0, 2), Point(-2, 0, 2), Point(-1, 0, 2), Point(0, 0, 2), Point(1, 0, 2), Point(2, 0, 2), Wall(3, 0, 2), Point(4, 0, 2), Wall(5, 0, 2),
            Wall(-5, 0, 3), Point(-4, 0, 3), Wall(-3, 0, 3), Wall(-2, 0, 3), Point(-1, 0, 3), Wall(0, 0, 3), Point(1, 0, 3), Wall(2, 0, 3), Wall(3, 0, 3), Point(4, 0, 3), Wall(5, 0, 3),
            Wall(-5, 0, 4), Point(-4, 0, 4), Point(-3, 0, 4), Point(-2, 0, 4), Point(-1, 0, 4), Wall(0, 0, 4), Point(1, 0, 4), Point(2, 0, 4), Point(3, 0, 4), Boost(4, 0, 4), Wall(5, 0, 4),
            Wall(-5, 0, 5), Wall(-4, 0, 5), Wall(-3, 0, 5), Wall(-2, 0, 5), Wall(-1, 0, 5), Wall(0, 0, 5), Wall(1, 0, 5), Wall(2, 0, 5), Wall(3, 0, 5), Wall(4, 0, 5), Wall(5, 0, 5)
        ]
        

        self.wallColor = pr.GRAY

    def draw_map(self):

        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(11, 11), pr.BLACK)

        for cell in self.map:
            cell.draw()

if __name__ == '__main__':
    map = Map()

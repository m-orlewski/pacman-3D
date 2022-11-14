import pyray as pr

from cell import Wall, Point, Boost, Tile
from pacman import Pacman

class Map():
    def __init__(self):
        self.walls = [
            Wall(-5, 0, -5), Wall(-4, 0, -5), Wall(-3, 0, -5), Wall(-2, 0, -5), Wall(-1, 0, -5), Wall(0, 0, -5), Wall(1, 0, -5), Wall(2, 0, -5), Wall(3, 0, -5), Wall(4, 0, -5), Wall(5, 0, -5),
            Wall(-5, 0, -4),  Wall(0, 0, -4),  Wall(5, 0, -4), Wall(-5, 0, -3),  Wall(-3, 0, -3), Wall(-2, 0, -3),  Wall(0, 0, -3),  Wall(2, 0, -3), Wall(3, 0, -3),  Wall(5, 0, -3),
            Wall(-5, 0, -2),  Wall(-3, 0, -2),  Wall(3, 0, -2),  Wall(5, 0, -2), Wall(-5, 0, -1),  Wall(-3, 0, -1),  Wall(-1, 0, -1), Wall(0, 0, -1), Wall(1, 0, -1),
            Wall(3, 0, -1),  Wall(5, 0, -1), Wall(-5, 0, 0),  Wall(5, 0, 0), Wall(-5, 0, 1),  Wall(-3, 0, 1),  Wall(-1, 0, 1), Wall(0, 0, 1), Wall(1, 0, 1),  Wall(3, 0, 1),  Wall(5, 0, 1),
            Wall(-5, 0, 2),  Wall(-3, 0, 2),  Wall(3, 0, 2),  Wall(5, 0, 2), Wall(-5, 0, 3),  Wall(-3, 0, 3), Wall(-2, 0, 3),  Wall(0, 0, 3),  Wall(2, 0, 3), Wall(3, 0, 3), Wall(5, 0, 3),
            Wall(-5, 0, 4),  Wall(0, 0, 4),  Wall(5, 0, 4), Wall(-5, 0, 5), Wall(-4, 0, 5), Wall(-3, 0, 5), Wall(-2, 0, 5), Wall(-1, 0, 5), Wall(0, 0, 5), Wall(1, 0, 5), Wall(2, 0, 5),
            Wall(3, 0, 5), Wall(4, 0, 5), Wall(5, 0, 5)
        ]

        self.points = [
            Boost(-4, 0, -4), Point(-3, 0, -4), Point(-2, 0, -4), Point(-1, 0, -4), Point(1, 0, -4), Point(2, 0, -4), Point(3, 0, -4), Point(4, 0, -4), Point(4, 0, -1), Point(4, 0, -2), Boost(4, 0, 4),
            Point(-4, 0, -3), Point(-1, 0, -3), Point(1, 0, -3), Point(4, 0, -3), Point(-4, 0, -2), Point(-2, 0, -2), Point(-1, 0, -2), Point(0, 0, -2), Point(1, 0, -2), Point(2, 0, -2), Point(-2, 0, -1),
            Point(-4, 0, -1), Point(-4, 0, 0), Point(-3, 0, 0), Point(-2, 0, 0), Point(-1, 0, 0), Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0), Point(4, 0, 0), Point(-4, 0, 1),
            Point(-2, 0, 1), Point(2, 0, 1), Point(4, 0, 1), Point(-4, 0, 2), Point(-2, 0, 2), Point(-1, 0, 2), Point(0, 0, 2), Point(1, 0, 2), Point(2, 0, 2),  Point(4, 0, 3), Point(2, 0, -1),
            Point(-4, 0, 4), Point(-3, 0, 4), Point(-2, 0, 4), Point(-1, 0, 4), Point(-4, 0, 3), Point(4, 0, 2), Point(-1, 0, 3), Point(1, 0, 3), Point(1, 0, 4), Point(2, 0, 4), Point(3, 0, 4), 
        ]

        self.pacman = Pacman()

    def update(self):
        if pr.is_key_down(pr.KEY_RIGHT):
            self.pacman.move_right(self.walls)
        elif pr.is_key_down(pr.KEY_LEFT):
            self.pacman.move_left(self.walls)
        elif pr.is_key_down(pr.KEY_DOWN):
            self.pacman.move_down(self.walls)
        elif pr.is_key_down(pr.KEY_UP):
            self.pacman.move_up(self.walls)

        i, boost_activated = self.pacman.collect_points(self.points)

        if i is not None:
            del self.points[i]

        if boost_activated:
            pass #TODO

    def draw(self):
        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(11, 11), pr.BLACK)

        for wall in self.walls:
            wall.draw()

        for point in self.points:
            point.draw()

        self.pacman.draw()

        

if __name__ == '__main__':
    map = Map()
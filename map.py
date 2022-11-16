import pyray as pr
from enum import Enum

from cell import Wall, Point, Boost
from pacman import Pacman
from ghost import Ghost

class GameState(Enum):
    GAMEPLAY = 0
    GAME_OVER = 1
    GAME_WON = 2

class Map():
    def __init__(self):

        #self.map =[
        #    [Wall(-5, 0, -5), Wall(-4, 0, -5), Wall(-3, 0, -5), Wall(-2, 0, -5), Wall(-1, 0, -5), Wall(0, 0, -5), Wall(1, 0, -5), Wall(2, 0, -5), Wall(3, 0, -5), Wall(4, 0, -5), Wall(5, 0, -5)],
        #    [Wall(-5, 0, -4), Boost(-4, 0, -4), Point(-3, 0, -4), Point(-2, 0, -4), Point(-1, 0, -4), Wall(0, 0, -4), Point(1, 0, -4), Point(2, 0, -4), Point(3, 0, -4), Point(4, 0, -4), Wall(5, 0, -4)],
        #    [Wall(-5, 0, -3), Point(-4, 0, -3), Wall(-3, 0, -3), Wall(-2, 0, -3), Point(-1, 0, -3), Wall(0, 0, -3), Point(1, 0, -3), Wall(2, 0, -3), Wall(3, 0, -3), Point(4, 0, -3), Wall(5, 0, -3)],
        #    [Wall(-5, 0, -2), Point(-4, 0, -2), Wall(-3, 0, -2), Point(-2, 0, -2), Point(-1, 0, -2), Point(0, 0, -2), Point(1, 0, -2), Point(2, 0, -2), Wall(3, 0, -2), Point(4, 0, -2), Wall(5, 0, -2)],
        #    [Wall(-5, 0, -1), Point(-4, 0, -1), Wall(-3, 0, -1), Point(-2, 0, -1), Wall(-1, 0, -1), Wall(0, 0, -1), Wall(1, 0, -1), Point(2, 0, -1), Wall(3, 0, -1), Point(4, 0, -1), Wall(5, 0, -1)],
        #    [Wall(-5, 0, 0), Point(-4, 0, 0), Point(-3, 0, 0), Point(-2, 0, 0), Point(-1, 0, 0), Point(0, 0, 0), Point(1, 0, 0), Point(2, 0, 0), Point(3, 0, 0), Point(4, 0, 0), Wall(5, 0, 0)],
        #    [Wall(-5, 0, 1), Point(-4, 0, 1), Wall(-3, 0, 1), Point(-2, 0, 1), Wall(-1, 0, 1), Wall(0, 0, 1), Wall(1, 0, 1), Point(2, 0, 1), Wall(3, 0, 1), Point(4, 0, 1), Wall(5, 0, 1)],
        #    [Wall(-5, 0, 2), Point(-4, 0, 2), Wall(-3, 0, 2), Point(-2, 0, 2), Point(-1, 0, 2), Point(0, 0, 2), Point(1, 0, 2), Point(2, 0, 2), Wall(3, 0, 2), Point(4, 0, 2), Wall(5, 0, 2)],
        #    [Wall(-5, 0, 3), Point(-4, 0, 3), Wall(-3, 0, 3), Wall(-2, 0, 3), Point(-1, 0, 3), Wall(0, 0, 3), Point(1, 0, 3), Wall(2, 0, 3), Wall(3, 0, 3), Point(4, 0, 3), Wall(5, 0, 3)],
        #    [Wall(-5, 0, 4), Point(-4, 0, 4), Point(-3, 0, 4), Point(-2, 0, 4), Point(-1, 0, 4), Wall(0, 0, 4), Point(1, 0, 4), Point(2, 0, 4), Point(3, 0, 4), Boost(4, 0, 4), Wall(5, 0, 4)],
        #    [Wall(-5, 0, 5), Wall(-4, 0, 5), Wall(-3, 0, 5), Wall(-2, 0, 5), Wall(-1, 0, 5), Wall(0, 0, 5), Wall(1, 0, 5), Wall(2, 0, 5), Wall(3, 0, 5), Wall(4, 0, 5), Wall(5, 0, 5)]
        #]

        self.map = [
            Wall(-7.5, 0, -7.5), Wall(-6, 0, -7.5), Wall(-4.5, 0, -7.5), Wall(-3, 0, -7.5), Wall(-1.5, 0, -7.5), Wall(0, 0, -7.5), Wall(1.5, 0, -7.5), Wall(3, 0, -7.5), Wall(4.5, 0, -7.5), Wall(6, 0, -7.5), Wall(7.5, 0, -7.5),
            Wall(-7.5, 0, -6), Boost(-6, 0, -6), Point(-4.5, 0, -6), Point(-3, 0, -6), Point(-1.5, 0, -6), Wall(0, 0, -6), Point(1.5, 0, -6), Point(3, 0, -6), Point(4.5, 0, -6), Point(6, 0, -6), Wall(7.5, 0, -6),
            Wall(-7.5, 0, -4.5), Point(-6, 0, -4.5), Wall(-4.5, 0, -4.5), Wall(-3, 0, -4.5), Point(-1.5, 0, -4.5), Wall(0, 0, -4.5), Point(1.5, 0, -4.5), Wall(3, 0, -4.5), Wall(4.5, 0, -4.5), Point(6, 0, -4.5), Wall(7.5, 0, -4.5),
            Wall(-7.5, 0, -3), Point(-6, 0, -3), Wall(-4.5, 0, -3), Point(-3, 0, -3), Point(-1.5, 0, -3), Point(0, 0, -3), Point(1.5, 0, -3), Point(3, 0, -3), Wall(4.5, 0, -3), Point(6, 0, -3), Wall(7.5, 0, -3),
            Wall(-7.5, 0, -1.5), Point(-6, 0, -1.5), Wall(-4.5, 0, -1.5), Point(-3, 0, -1.5), Wall(-1.5, 0, -1.5), Wall(0, 0, -1.5), Wall(1.5, 0, -1.5), Point(3, 0, -1.5), Wall(4.5, 0, -1.5), Point(6, 0, -1.5), Wall(7.5, 0, -1.5),
            Wall(-7.5, 0, 0), Point(-6, 0, 0), Point(-4.5, 0, 0), Point(-3, 0, 0), Point(-1.5, 0, 0), Point(0, 0, 0), Point(1.5, 0, 0), Point(3, 0, 0), Point(4.5, 0, 0), Point(6, 0, 0), Wall(7.5, 0, 0),
            Wall(-7.5, 0, 1.5), Point(-6, 0, 1.5), Wall(-4.5, 0, 1.5), Point(-3, 0, 1.5), Wall(-1.5, 0, 1.5), Wall(0, 0, 1.5), Wall(1.5, 0, 1.5), Point(3, 0, 1.5), Wall(4.5, 0, 1.5), Point(6, 0, 1.5), Wall(7.5, 0, 1.5),
            Wall(-7.5, 0, 3), Point(-6, 0, 3), Wall(-4.5, 0, 3), Point(-3, 0, 3), Point(-1.5, 0, 3), Point(0, 0, 3), Point(1.5, 0, 3), Point(3, 0, 3), Wall(4.5, 0, 3), Point(6, 0, 3), Wall(7.5, 0, 3),
            Wall(-7.5, 0, 4.5), Point(-6, 0, 4.5), Wall(-4.5, 0, 4.5), Wall(-3, 0, 4.5), Point(-1.5, 0, 4.5), Wall(0, 0, 4.5), Point(1.5, 0, 4.5), Wall(3, 0, 4.5), Wall(4.5, 0, 4.5), Point(6, 0, 4.5), Wall(7.5, 0, 4.5),
            Wall(-7.5, 0, 6), Point(-6, 0, 6), Point(-4.5, 0, 6), Point(-3, 0, 6), Point(-1.5, 0, 6), Wall(0, 0, 6), Point(1.5, 0, 6), Point(3, 0, 6), Point(4.5, 0, 6), Boost(6, 0, 6), Wall(7.5, 0, 6),
            Wall(-7.5, 0, 7.5), Wall(-6, 0, 7.5), Wall(-4.5, 0, 7.5), Wall(-3, 0, 7.5), Wall(-1.5, 0, 7.5), Wall(0, 0, 7.5), Wall(1.5, 0, 7.5), Wall(3, 0, 7.5), Wall(4.5, 0, 7.5), Wall(6, 0, 7.5), Wall(7.5, 0, 7.5)
        ]


        self.walls = []
        self.points = []
        for cell in self.map:
            if type(cell) == Wall:
                self.walls.append(cell)
            else:
                self.points.append(cell)

        self.pacman = Pacman()
        self.score = 0

        self.red = Ghost(6, 0, 6, 0, 'models/red.vox')
        self.orange = Ghost(-6, 0, -6, 2, 'models/orange.vox')
        self.cyan = Ghost(-6, 0, 6, 1, 'models/cyan.vox')
        self.pink = Ghost(6, 0, -6, 3, 'models/pink.vox')

    def update(self):
        # update pacman movement
        if pr.is_key_down(pr.KEY_RIGHT):
            self.pacman.move_right(self.walls)
        elif pr.is_key_down(pr.KEY_LEFT):
            self.pacman.move_left(self.walls)
        elif pr.is_key_down(pr.KEY_DOWN):
            self.pacman.move_down(self.walls)
        elif pr.is_key_down(pr.KEY_UP):
            self.pacman.move_up(self.walls)

        # move ghosts
        self.red.move(self.walls)
        self.orange.move(self.walls)
        self.cyan.move(self.walls)
        self.pink.move(self.walls)

        # check if game over
        if self.pacman.check_ghost_collsions(self.red, self.orange, self.cyan, self.pink):
            return GameState.GAME_OVER

        # collect points
        i, boost_activated = self.pacman.collect_points(self.points)

        # check if game won
        if i is not None:
            del self.points[i]
            self.score += 1

            if len(self.points) == 0:
                return GameState.GAME_WON

        if boost_activated:
            pass #TODO
        
        return GameState.GAMEPLAY

    def draw(self):
        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(16.5, 16.5), pr.BLACK)

        for wall in self.walls:
            wall.draw()

        for point in self.points:
            point.draw()

        self.pacman.draw()
        
        self.red.draw()
        self.orange.draw()
        self.cyan.draw()
        self.pink.draw()
        

if __name__ == '__main__':
    map = Map()
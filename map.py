import pyray as pr
from enum import Enum
import math

from cell import Wall, Point, Boost, CELL_SIZE
from pacman import Pacman
from ghost import Ghost

BOOST_TIME = 5

class GameState(Enum):
    GAMEPLAY = 0
    GAME_OVER = 1
    GAME_WON = 2

class Map():
    def __init__(self):

        self.map = []
        self.mapWidth = 17
        self.mapHeight = 11
        with open('map.dat', 'r') as mapFile:        
            m2 = -math.floor(self.mapHeight/2)
            for line in mapFile:
                m1 = -math.floor(self.mapWidth/2)
                for c in line:
                    if c == '#':
                        self.map.append(Wall(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    elif c == '*':
                        self.map.append(Point(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    elif c == '$':
                        self.map.append(Boost(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    m1 += 1
                m2 += 1

        '''        self.map = [
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
        ]'''


        self.walls = []
        self.points = []
        for cell in self.map:
            if type(cell) == Wall:
                self.walls.append(cell)
            else:
                self.points.append(cell)

        self.pacman = Pacman()
        self.score = 0

        self.ghosts = [Ghost(10.5, 0, 6, 0, 'models/red.vox'), Ghost(-10.5, 0, -6, 2, 'models/orange.vox'), Ghost(-10.5, 0, 6, 1, 'models/cyan.vox'), Ghost(10.5, 0, -6, 3, 'models/pink.vox')]

        self.scatterMode = False

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
        for ghost in self.ghosts:
            ghost.move(self.walls)

        # check if game over
        if self.pacman.check_ghost_collsions(self.ghosts, self.scatterMode):
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
            if self.scatterMode:
                self.startTime = pr.get_time()
            else:
                self.scatterMode = True
                for ghost in self.ghosts:
                    ghost.change_scatter_mode()
                    self.startTime = pr.get_time()

        if self.scatterMode:
            currentTime = pr.get_time()
            if currentTime - self.startTime >= BOOST_TIME:
                self.scatterMode = False
                for ghost in self.ghosts:
                    ghost.change_scatter_mode()
        
        return GameState.GAMEPLAY

    def draw(self):
        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(self.mapWidth*CELL_SIZE, self.mapHeight*CELL_SIZE), pr.BLACK)

        for wall in self.walls:
            wall.draw()

        for point in self.points:
            point.draw()

        self.pacman.draw()
        
        for ghost in self.ghosts:
            ghost.draw()
        

if __name__ == '__main__':
    map = Map()
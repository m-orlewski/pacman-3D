import pyray as pr
from enum import Enum
import math

from cell import Wall, Point, Boost, CELL_SIZE
from pacman import Pacman
from ghost import Ghost

BOOST_TIME = 5

class GameState(Enum):
    MENU = 0
    GAMEPLAY = 1
    GAME_OVER = 2
    GAME_WON = 3

class Map():
    def __init__(self):

        # read map from file
        map = []
        with open('maps/map2.dat', 'r') as mapFile:     
            mapSize = mapFile.readline().strip().split()
            self.mapWidth = int(mapSize[0])
            self.mapHeight = int(mapSize[1])
            m2 = -math.floor(self.mapHeight/2)
            for line in mapFile:
                m1 = -math.floor(self.mapWidth/2)
                for c in line:
                    if c == '#':
                        map.append(Wall(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    elif c == '*':
                        map.append(Point(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    elif c == '$':
                        map.append(Boost(CELL_SIZE * m1, 0, CELL_SIZE*m2))
                    m1 += 1
                m2 += 1

        # split map into walls and points
        self.walls = []
        self.points = []
        for cell in map:
            if type(cell) == Wall:
                self.walls.append(cell)
            else:
                self.points.append(cell)

        # create pacman
        self.pacman = Pacman()
        self.score = 0


        # create ghosts
        m1 = math.floor(self.mapWidth/2)-1
        m2 = math.floor(self.mapHeight/2)-1
        self.ghosts = [Ghost(m1*CELL_SIZE, 0, m2*CELL_SIZE, 0, 'models/red.vox'), Ghost(-m1*CELL_SIZE, 0, -m2*CELL_SIZE, 2, 'models/orange.vox'),
                       Ghost(-m1*CELL_SIZE, 0, m2*CELL_SIZE, 1, 'models/cyan.vox'), Ghost(m1*CELL_SIZE, 0, -m2*CELL_SIZE, 3, 'models/pink.vox')]
        self.scatterMode = False

    def update(self):
        '''Update map state'''

        # move pacman
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

        # check if game won, score points
        if i is not None:
            del self.points[i]
            self.score += 1

            if len(self.points) == 0:
                return GameState.GAME_WON

        # activate/prolong boost
        if boost_activated:
            if self.scatterMode:
                self.startTime = pr.get_time()
            else:
                self.scatterMode = True
                for ghost in self.ghosts:
                    ghost.change_scatter_mode()
                    self.startTime = pr.get_time()

        # check if boost is over
        if self.scatterMode:
            currentTime = pr.get_time()
            if currentTime - self.startTime >= BOOST_TIME:
                self.scatterMode = False
                for ghost in self.ghosts:
                    ghost.change_scatter_mode()
        
        return GameState.GAMEPLAY

    def draw(self):
        ''' Draw map'''
        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(self.mapWidth*CELL_SIZE, self.mapHeight*CELL_SIZE), pr.BLACK)

        for wall in self.walls:
            wall.draw()

        for point in self.points:
            point.draw()

        self.pacman.draw()
        
        for ghost in self.ghosts:
            ghost.draw()
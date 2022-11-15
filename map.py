import pyray as pr
from enum import Enum
import math

from cell import Wall, Point, Boost
from pacman import Pacman
from ghost import Ghost

class GameState(Enum):
    GAMEPLAY = 0
    GAME_OVER = 1
    GAME_WON = 2

class Map():
    def __init__(self, map):

        self.map = []
        self.mapHeight = 11
        self.mapWidth = 11
        
        for i, line in enumerate(map.splitlines()):
            self.map.append([])
            for j, c in enumerate(line):
                if c == '#':
                    self.map[i].append(Wall(i, j, self.mapWidth, self.mapHeight))
                elif c == '*':
                    self.map[i].append(Point(i, j, self.mapWidth, self.mapHeight))
                elif c == '@':
                    self.map[i].append(Boost(i, j, self.mapWidth, self.mapHeight))



        self.pacman = Pacman(math.floor(self.mapWidth/2), math.floor(self.mapHeight/2), self.mapWidth, self.mapHeight)
        self.map[self.pacman.i][self.pacman.j].collected = False
        self.score = 0
        self.totalScore = map.count('*') + map.count('@')

        self.red = Ghost(self.mapWidth-2, self.mapHeight-2, self.mapWidth, self.mapHeight, pr.RED, 0)
        self.orange = Ghost(1, 1, self.mapWidth, self.mapHeight, pr.ORANGE, 2)
        self.cyan = Ghost(self.mapWidth-2, 1, self.mapWidth, self.mapHeight, pr.Color(0, 255, 255, 255), 1)
        self.pink = Ghost(1, self.mapHeight-2, self.mapWidth, self.mapHeight, pr.PINK, 3)

    def update(self):
        # update pacman movement
        if pr.is_key_down(pr.KEY_RIGHT):
            self.pacman.move_right(self.map)
        if pr.is_key_down(pr.KEY_LEFT):
            self.pacman.move_left(self.map)
        if pr.is_key_down(pr.KEY_DOWN):
            self.pacman.move_down(self.map)
        if pr.is_key_down(pr.KEY_UP):
            self.pacman.move_up(self.map)

        # check if game over
        if self.pacman.check_ghost_collsions(self.red, self.orange, self.cyan, self.pink):
            return GameState.GAME_OVER

        # collect points
        pointCollected, boostCollected = self.pacman.collect_points(self.map)

        # check if game won
        if pointCollected:
            self.score += 1

            if self.score == self.totalScore:
                return GameState.GAME_WON

        if boostCollected:
            pass #TODO

        # move ghosts
        self.red.move(self.map)
        self.orange.move(self.map)
        self.cyan.move(self.map)
        self.pink.move(self.map)
        
        return GameState.GAMEPLAY

    def draw(self):
        pr.draw_plane(pr.Vector3(0, -0.5, 0), pr.Vector2(self.mapWidth, self.mapHeight), pr.BLACK)

        for row in self.map:
            for cell in row:
                cell.draw()

        self.pacman.draw()
        
        self.red.draw()
        self.orange.draw()
        self.cyan.draw()
        self.pink.draw()
        

if __name__ == '__main__':
    map = Map()
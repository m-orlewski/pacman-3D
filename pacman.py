import pyray as pr
import math

from cell import Point, Boost, Wall, CELL_SIZE, POINT_RADIUS, BOOST_RADIUS
from ghost import GHOST_RADIUS

PACMAN_RADIUS = 0.4
PACMAN_SPEED = 0.075

class Pacman():
    def __init__(self, i, j, mapWidth, mapHeight):
        self.i = i
        self.j = j
        self.pos = pr.Vector3(0, 0, 0)
        self.mapWidth = mapWidth
        self.mapHeight = mapHeight

    def draw(self):
        pr.draw_sphere(self.pos, PACMAN_RADIUS, pr.YELLOW)

    def move_right(self, map):
        newPos = pr.Vector3(self.pos.x + PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(map, newPos):
            self.pos.x = newPos.x
            self.update_index()

    def move_left(self, map):
        newPos = pr.Vector3(self.pos.x - PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(map, newPos):
            self.pos.x = newPos.x
            self.update_index()

    def move_up(self, map):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - PACMAN_SPEED)
        if not self.check_collisions(map, newPos):
            self.pos.z = newPos.z
            self.update_index()

    def move_down(self, map):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + PACMAN_SPEED)
        if not self.check_collisions(map, newPos):
            self.pos.z = newPos.z
            self.update_index()

    def check_collisions(self, map, newPos):
        cells = [map[self.i-1][self.j-1], map[self.i][self.j-1], map[self.i+1][self.j-1], map[self.i-1][self.j], map[self.i][self.j], map[self.i+1][self.j], map[self.i-1][self.j+1], map[self.i][self.j+1], map[self.i+1][self.j+1]]
        for cell in cells:
            if type(cell) == Wall:
                boudingBox = pr.BoundingBox(pr.Vector3(cell.pos.x - CELL_SIZE/2, cell.pos.y - CELL_SIZE/2, cell.pos.z - CELL_SIZE/2),
                                            pr.Vector3(cell.pos.x + CELL_SIZE/2, cell.pos.y + CELL_SIZE/2, cell.pos.z + CELL_SIZE/2))
                if pr.check_collision_box_sphere(boudingBox, newPos, PACMAN_RADIUS):
                    return True
        return False

    def collect_points(self, map):
        point = map[self.i][self.j]
        print(self.i, self.j)
        if type(point) == Point and not point.collected:
            if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, POINT_RADIUS):
                point.collected = True
                return (True, False)
        elif type(point) == Boost and not point.collected:
            if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, BOOST_RADIUS):
                point.collected = True
                return (True, True)

        return (False, False)

    def check_ghost_collsions(self, red, orange, cyan, pink):
        if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, red.pos, GHOST_RADIUS):
            return True
        elif pr.check_collision_spheres(self.pos, PACMAN_RADIUS, orange.pos, GHOST_RADIUS):
            return True
        elif pr.check_collision_spheres(self.pos, PACMAN_RADIUS, cyan.pos, GHOST_RADIUS):
            return True
        elif pr.check_collision_spheres(self.pos, PACMAN_RADIUS, pink.pos, GHOST_RADIUS):
            return True
        return False

    def update_index(self):
        self.j = round(self.pos.x + (math.floor(self.mapWidth/2)))
        self.i = round(self.pos.z + (math.floor(self.mapHeight/2)))

                




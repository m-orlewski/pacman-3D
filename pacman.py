import pyray as pr

from cell import Point, Boost, CELL_SIZE, POINT_RADIUS, BOOST_RADIUS
from ghost import GHOST_RADIUS

PACMAN_RADIUS = 0.4
PACMAN_SPEED = 0.075

class Pacman():
    def __init__(self):
        self.pos = pr.Vector3(0, 0.4, 0)

    def draw(self):
        pr.draw_sphere(self.pos, PACMAN_RADIUS, pr.YELLOW)

    def move_right(self, walls):
        newPos = pr.Vector3(self.pos.x + PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_left(self, walls):
        newPos = pr.Vector3(self.pos.x - PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_up(self, walls):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - PACMAN_SPEED)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def move_down(self, walls):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + PACMAN_SPEED)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def check_collisions(self, walls, newPos):
        for wall in walls:
            boudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            if pr.check_collision_box_sphere(boudingBox, newPos, PACMAN_RADIUS):
                return True
        return False

    def collect_points(self, points):
        for i, point in enumerate(points):
            if type(point) == Point:
                if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, POINT_RADIUS):
                    return (i, False)
            elif type(point) == Boost:
                if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, BOOST_RADIUS):
                    return (i, True)

        return (None, False)

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

                




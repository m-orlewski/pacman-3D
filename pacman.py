import pyray as pr

from cell import Point, Boost, CELL_SIZE, POINT_RADIUS, BOOST_RADIUS

PACMAN_RADIUS = 0.6
PACMAN_SPEED = 0.075

class Pacman():
    '''Class representing pacman'''

    def __init__(self):
        self.pos = pr.Vector3(0, 0.6, 0)
        self.currentDirection = 0 # direction pacman is currently moving

    def draw(self):
        '''Draw pacman'''

        pr.draw_sphere(self.pos, PACMAN_RADIUS, pr.YELLOW)
        if self.currentDirection == 0:
            pr.draw_sphere(pr.Vector3(self.pos.x+PACMAN_RADIUS/3, 1.5*PACMAN_RADIUS, self.pos.z-0.9*PACMAN_RADIUS), PACMAN_RADIUS/4, pr.BLACK)
            pr.draw_sphere(pr.Vector3(self.pos.x-PACMAN_RADIUS/3, 1.5*PACMAN_RADIUS, self.pos.z-0.9*PACMAN_RADIUS), PACMAN_RADIUS/4, pr.BLACK)
        elif self.currentDirection == 1:
            pr.draw_sphere(pr.Vector3(self.pos.x+0.9*PACMAN_RADIUS, 1.5*PACMAN_RADIUS, self.pos.z+PACMAN_RADIUS/3), PACMAN_RADIUS/4, pr.BLACK)
            pr.draw_sphere(pr.Vector3(self.pos.x+0.9*PACMAN_RADIUS, 1.5*PACMAN_RADIUS, self.pos.z-PACMAN_RADIUS/3), PACMAN_RADIUS/4, pr.BLACK)
        elif self.currentDirection == 2:
            pr.draw_sphere(pr.Vector3(self.pos.x+PACMAN_RADIUS/3, 1.5*PACMAN_RADIUS, self.pos.z+0.9*PACMAN_RADIUS), PACMAN_RADIUS/4, pr.BLACK)
            pr.draw_sphere(pr.Vector3(self.pos.x-PACMAN_RADIUS/3, 1.5*PACMAN_RADIUS, self.pos.z+0.9*PACMAN_RADIUS), PACMAN_RADIUS/4, pr.BLACK)
        elif self.currentDirection == 3:
            pr.draw_sphere(pr.Vector3(self.pos.x-0.9*PACMAN_RADIUS, 1.5*PACMAN_RADIUS, self.pos.z+PACMAN_RADIUS/3), PACMAN_RADIUS/4, pr.BLACK)
            pr.draw_sphere(pr.Vector3(self.pos.x-0.9*PACMAN_RADIUS, 1.5*PACMAN_RADIUS, self.pos.z-PACMAN_RADIUS/3), PACMAN_RADIUS/4, pr.BLACK)

    def move_right(self, walls):
        '''Try to move pacman right'''

        self.currentDirection = 1
        newPos = pr.Vector3(self.pos.x + PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_left(self, walls):
        '''Try to move pacman left'''

        self.currentDirection = 3
        newPos = pr.Vector3(self.pos.x - PACMAN_SPEED, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_up(self, walls):
        '''Try to move pacman up'''

        self.currentDirection = 0
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - PACMAN_SPEED)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def move_down(self, walls):
        '''Try to move pacman down'''

        self.currentDirection = 2
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + PACMAN_SPEED)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def check_collisions(self, walls, newPos):
        '''Check for pacman collisions with walls'''

        for wall in walls:
            boudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            if pr.check_collision_box_sphere(boudingBox, newPos, PACMAN_RADIUS):
                return True
        return False

    def collect_points(self, points):
        '''
            Check if pacman collected points or boosts
            Returns index of collected point or None and True if collected point was a boost else False
        '''

        for i, point in enumerate(points):
            if type(point) == Point:
                if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, POINT_RADIUS):
                    return (i, False)
            elif type(point) == Boost:
                if pr.check_collision_spheres(self.pos, PACMAN_RADIUS, point.pos, BOOST_RADIUS):
                    return (i, True)

        return (None, False)

    def check_ghost_collsions(self, ghosts, scatterMode):
        '''
            Check for collisions with ghosts
        '''
        for ghost in ghosts:
            if not ghost.isEaten and pr.check_collision_box_sphere(ghost.bb, self.pos, PACMAN_RADIUS): # skip ghosts that are dead and waiting for respawn
                if scatterMode:
                    self.eat_ghost(ghost)
                else:
                    return True
        return False

    def eat_ghost(self, ghost):
        '''Eat a ghost'''
        ghost.ghost_death()

                




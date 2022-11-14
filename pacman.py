import pyray as pr

from cell import CELL_SIZE

PACMAN_RADIUS = 0.4
VELOCITY = 0.075

class Pacman():
    def __init__(self):
        self.pos = pr.Vector3(0, 0.4, 0)

    def draw(self):
        pr.draw_sphere(self.pos, PACMAN_RADIUS, pr.YELLOW)

    def move_right(self, walls):
        newPos = pr.Vector3(self.pos.x + VELOCITY, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_left(self, walls):
        newPos = pr.Vector3(self.pos.x - VELOCITY, self.pos.y, self.pos.z)
        if not self.check_collisions(walls, newPos):
            self.pos.x = newPos.x

    def move_up(self, walls):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - VELOCITY)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def move_down(self, walls):
        newPos = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + VELOCITY)
        if not self.check_collisions(walls, newPos):
            self.pos.z = newPos.z

    def check_collisions(self, walls, newPos):
        for wall in walls:
            boudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            if pr.check_collision_box_sphere(boudingBox, newPos, PACMAN_RADIUS):
                return True
        return False



import pyray as pr
import random
import time

from cell import CELL_SIZE

GHOST_RADIUS = 0.4
GHOST_SPEED = 0.05

class Ghost():
    def __init__(self, x, y, z, color, currentDirection):
        self.pos = pr.Vector3(x, y, z)
        self.color = color

        self.currentDirection = currentDirection
        self.stepCount = 0

    def draw(self):
        pr.draw_sphere(self.pos, GHOST_RADIUS, self.color)

    def check_collisions(self, walls, newPos):
        for wall in walls:
            boudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            if pr.check_collision_box_sphere(boudingBox, newPos, GHOST_RADIUS):
                return True
        return False

    def updateDirection(self, walls):        
        newPosUp = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - GHOST_SPEED)
        newPosRight = pr.Vector3(self.pos.x + GHOST_SPEED, self.pos.y, self.pos.z)
        newPosDown = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + GHOST_SPEED)
        newPosUp = pr.Vector3(self.pos.x - GHOST_SPEED, self.pos.y, self.pos.z)

        
            

    def move(self, walls):
        if self.stepCount == 20:
            self.updateDirection(walls)

        if self.currentDirection == 0:
            self.pos.z -= GHOST_SPEED
        elif self.currentDirection == 1:
            self.pos.x += GHOST_SPEED
        elif self.currentDirection == 2:
            self.pos.z += GHOST_SPEED
        elif self.currentDirection == 3:
            self.pos.x -= GHOST_SPEED

        self.stepCount += 1

        
        
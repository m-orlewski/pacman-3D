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
        self.oppositeDirection = (self.currentDirection + 2) % 4
        self.stepCount = 0

    def draw(self):
        pr.draw_sphere(self.pos, GHOST_RADIUS, self.color)

    def check_collisions(self, walls, newPos):
        for wall in walls:
            wallBoudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            ghostBoundingBox = pr.BoundingBox(pr.Vector3(newPos.x - CELL_SIZE/2 + 0.0001, newPos.y - CELL_SIZE/2 + 0.0001, newPos.z - CELL_SIZE/2 + 0.0001),
                                        pr.Vector3(newPos.x + CELL_SIZE/2 - 0.0001, newPos.y + CELL_SIZE/2 - 0.0001, newPos.z + CELL_SIZE/2 - 0.0001))
            if pr.check_collision_boxes(wallBoudingBox, ghostBoundingBox):
                return False
        return True

    def updateDirection(self, walls):        
        newPosUp = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - GHOST_SPEED)
        newPosRight = pr.Vector3(self.pos.x + GHOST_SPEED, self.pos.y, self.pos.z)
        newPosDown = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + GHOST_SPEED)
        newPosLeft = pr.Vector3(self.pos.x - GHOST_SPEED, self.pos.y, self.pos.z)

        canMove = [self.check_collisions(walls, newPosUp), self.check_collisions(walls, newPosRight), self.check_collisions(walls, newPosDown),self.check_collisions(walls, newPosLeft)]
        print(canMove)
        if canMove.count(True) == 2 and canMove[self.currentDirection] and canMove[self.oppositeDirection]:
            return # can only go the same direction or turn back, so go ahead
        elif canMove.count(True) == 1:
            self.currentDirection, self.oppositeDirection = self.oppositeDirection, self.currentDirection # in case of dead end, turn back
        else:
            canMove[self.oppositeDirection] = False
            availableDirections = [i for i, value in enumerate(canMove) if value == True]
            print(availableDirections)
            self.currentDirection = random.choice(availableDirections)
            self.oppositeDirection = (self.currentDirection + 2) % 4

    def move(self, walls):
        if self.stepCount == 20:
            self.updateDirection(walls)
            self.stepCount = 0

        if self.currentDirection == 0:
            self.pos.z -= GHOST_SPEED
        elif self.currentDirection == 1:
            self.pos.x += GHOST_SPEED
        elif self.currentDirection == 2:
            self.pos.z += GHOST_SPEED
        elif self.currentDirection == 3:
            self.pos.x -= GHOST_SPEED

        self.stepCount += 1

        
        
import pyray as pr
import random
import math

from cell import Wall, CELL_SIZE

GHOST_RADIUS = 0.4
GHOST_SPEED = 0.01

class Ghost():
    def __init__(self, i, j, mapWidth, mapHeight, color, currentDirection):
        self.i = i
        self.j = j
        self.pos = pr.Vector3(j - (math.floor(mapWidth/2)), 0, i - (math.floor(mapHeight/2)))
        self.color = color

        self.currentDirection = currentDirection
        self.oppositeDirection = (self.currentDirection + 2) % 4
        self.stepCount = 0

        self.mapWidth = mapWidth
        self.mapHeight = mapHeight

    def draw(self):
        pr.draw_sphere(self.pos, GHOST_RADIUS, self.color)

    def check_collisions(self, map, newPos):
        cells = [map[self.i-1][self.j-1], map[self.i][self.j-1], map[self.i+1][self.j-1], map[self.i-1][self.j], map[self.i][self.j], map[self.i+1][self.j], map[self.i-1][self.j+1], map[self.i][self.j+1], map[self.i+1][self.j+1]]
        for cell in cells:
            if type(cell) == Wall:
                wallBoudingBox = pr.BoundingBox(pr.Vector3(cell.pos.x - CELL_SIZE/2, cell.pos.y - CELL_SIZE/2, cell.pos.z - CELL_SIZE/2),
                                            pr.Vector3(cell.pos.x + CELL_SIZE/2, cell.pos.y + CELL_SIZE/2, cell.pos.z + CELL_SIZE/2))
                ghostBoundingBox = pr.BoundingBox(pr.Vector3(newPos.x - CELL_SIZE/2 + 0.0001, newPos.y - CELL_SIZE/2 + 0.0001, newPos.z - CELL_SIZE/2 + 0.0001),
                                            pr.Vector3(newPos.x + CELL_SIZE/2 - 0.0001, newPos.y + CELL_SIZE/2 - 0.0001, newPos.z + CELL_SIZE/2 - 0.0001))
                if pr.check_collision_boxes(wallBoudingBox, ghostBoundingBox):
                    return False
        return True

    def updateDirection(self, map):        
        newPosUp = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - GHOST_SPEED)
        newPosRight = pr.Vector3(self.pos.x + GHOST_SPEED, self.pos.y, self.pos.z)
        newPosDown = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + GHOST_SPEED)
        newPosLeft = pr.Vector3(self.pos.x - GHOST_SPEED, self.pos.y, self.pos.z)

        canMove = [self.check_collisions(map, newPosUp), self.check_collisions(map, newPosRight), self.check_collisions(map, newPosDown),self.check_collisions(map, newPosLeft)]
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

    def move(self, map):
        if self.stepCount == 100:
            self.updateDirection(map)
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
        self.update_index()

    def update_index(self):
        self.j = round(self.pos.x + (math.floor(self.mapWidth/2)))
        self.i = round(self.pos.z + (math.floor(self.mapHeight/2)))

        
        
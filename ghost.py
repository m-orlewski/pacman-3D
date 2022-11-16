import pyray as pr
import random
import math

from cell import CELL_SIZE

GHOST_RADIUS = 0.7
GHOST_SPEED = 0.05
RESPAWN_TIME = 5

class Ghost():
    def __init__(self, x, y, z, currentDirection, voxFileName):
        self.voxFileName = voxFileName
        self.pos = pr.Vector3(x, y, z)

        self.previousDirection = 2
        self.currentDirection = currentDirection
        self.oppositeDirection = (self.currentDirection + 2) % 4
        self.stepCount = 0

        self.scatterMode = False
        self.isEaten = False

        self.load_model()

    def draw(self):
        if not self.isEaten:
            pr.draw_model(self.model, self.pos, 1.0, pr.WHITE)
            self.bb = pr.BoundingBox(pr.Vector3(self.pos.x - GHOST_RADIUS, self.pos.y - GHOST_RADIUS, self.pos.z - GHOST_RADIUS), pr.Vector3(self.pos.x + GHOST_RADIUS, self.pos.y + GHOST_RADIUS, self.pos.z + GHOST_RADIUS))

    def turn_model(self):
        if self.currentDirection == 0:
            mat_rotate = pr.matrix_rotate_y(math.radians(180))
        elif self.currentDirection == 1:
            mat_rotate = pr.matrix_rotate_y(math.radians(90))
        elif self.currentDirection == 2:
            mat_rotate = pr.matrix_rotate_y(math.radians(0))
        elif self.currentDirection == 3:
            mat_rotate = pr.matrix_rotate_y(math.radians(-90))

        self.model.transform = pr.matrix_multiply(self.mat_translate, mat_rotate)

    def load_model(self):
        self.model = pr.load_model(self.voxFileName)
        self.bb = pr.get_model_bounding_box(self.model)
        self.center = pr.Vector3(self.bb.min.x + (((self.bb.max.x - self.bb.min.x)/2)), 0, self.bb.min.z + (((self.bb.max.z - self.bb.min.z)/2)))
        self.mat_translate = pr.matrix_translate(-self.center.x, 0, -self.center.z)
        rotation_mult = max(self.currentDirection, self.previousDirection) - min(self.currentDirection, self.previousDirection)
        if self.previousDirection < self.currentDirection:
            mat_rotate = pr.matrix_rotate_y(math.radians(-1*rotation_mult*90))
        else:
            mat_rotate = pr.matrix_rotate_y(math.radians(rotation_mult*90))
        self.model.transform = pr.matrix_multiply(self.mat_translate, mat_rotate)

    def load_scatter_model(self):
        self.model = pr.load_model('models/scatter.vox')
        self.bb = pr.get_model_bounding_box(self.model)
        self.center = pr.Vector3(self.bb.min.x + (((self.bb.max.x - self.bb.min.x)/2)), 0, self.bb.min.z + (((self.bb.max.z - self.bb.min.z)/2)))
        self.mat_translate = pr.matrix_translate(-self.center.x, 0, -self.center.z)
        rotation_mult = max(self.currentDirection, self.previousDirection) - min(self.currentDirection, self.previousDirection)
        if self.previousDirection < self.currentDirection:
            mat_rotate = pr.matrix_rotate_y(math.radians(-1*rotation_mult*90))
        else:
            mat_rotate = pr.matrix_rotate_y(math.radians(rotation_mult*90))
        self.model.transform = pr.matrix_multiply(self.mat_translate, mat_rotate)


    def check_collisions(self, walls, newPos):
        for wall in walls:
            wallBoudingBox = pr.BoundingBox(pr.Vector3(wall.pos.x - CELL_SIZE/2, wall.pos.y - CELL_SIZE/2, wall.pos.z - CELL_SIZE/2),
                                        pr.Vector3(wall.pos.x + CELL_SIZE/2, wall.pos.y + CELL_SIZE/2, wall.pos.z + CELL_SIZE/2))
            ghostBoundingBox = pr.BoundingBox(pr.Vector3(newPos.x - CELL_SIZE/2 + 0.0001, newPos.y - CELL_SIZE/2 + 0.0001, newPos.z - CELL_SIZE/2 + 0.0001),
                                        pr.Vector3(newPos.x + CELL_SIZE/2 - 0.0001, newPos.y + CELL_SIZE/2 - 0.0001, newPos.z + CELL_SIZE/2 - 0.0001))
            if pr.check_collision_boxes(wallBoudingBox, ghostBoundingBox):
                return False
        return True

    def update_direction(self, walls):        
        newPosUp = pr.Vector3(self.pos.x, self.pos.y, self.pos.z - GHOST_SPEED)
        newPosRight = pr.Vector3(self.pos.x + GHOST_SPEED, self.pos.y, self.pos.z)
        newPosDown = pr.Vector3(self.pos.x, self.pos.y, self.pos.z + GHOST_SPEED)
        newPosLeft = pr.Vector3(self.pos.x - GHOST_SPEED, self.pos.y, self.pos.z)

        canMove = [self.check_collisions(walls, newPosUp), self.check_collisions(walls, newPosRight), self.check_collisions(walls, newPosDown),self.check_collisions(walls, newPosLeft)]

        if canMove.count(True) == 2 and canMove[self.currentDirection] and canMove[self.oppositeDirection]:
            return # can only go the same direction or turn back, so go ahead
        elif canMove.count(True) == 1:
            self.previousDirection = self.currentDirection
            self.currentDirection, self.oppositeDirection = self.oppositeDirection, self.currentDirection # in case of dead end, turn back
            self.turn_model()
        else:
            canMove[self.oppositeDirection] = False
            availableDirections = [i for i, value in enumerate(canMove) if value == True]
            self.previousDirection = self.currentDirection
            self.currentDirection = random.choice(availableDirections)
            self.oppositeDirection = (self.currentDirection + 2) % 4
            self.turn_model()

    def move(self, walls):
        if self.isEaten:
            currentTime = pr.get_time()
            if currentTime - self.deathTime >= RESPAWN_TIME:
                self.stepCount = 0
                self.respawn()
            else:
                return

        if self.stepCount == CELL_SIZE/GHOST_SPEED:
            self.update_direction(walls)
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

    def change_scatter_mode(self):
        if self.scatterMode:
            self.scatterMode = False
            self.load_model()
            self.turn_model()
        else:
            self.scatterMode = True
            self.previousDirection = self.currentDirection
            self.currentDirection, self.oppositeDirection = self.oppositeDirection, self.currentDirection
            self.load_scatter_model()
            self.stepCount = CELL_SIZE/GHOST_SPEED - self.stepCount

    def ghost_death(self):
        self.isEaten = True
        self.deathTime = pr.get_time()
        self.pos = pr.Vector3(0, 0, 0) # move to respawn

    def respawn(self):
        self.isEaten = False
        self.currentDirection = 0
        self.oppositeDirection = 2
        self.previousDirection = 2
        self.turn_model()



        
        
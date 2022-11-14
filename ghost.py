import pyray as pr

GHOST_RADIUS = 0.35
GHOST_SPEED = 0.05

class Ghost():
    def __init__(self, x, y, z, color):
        self.pos = pr.Vector3(x, y, z)
        self.color = color

        self.canMoveLeft = False
        self.canMoveRight = False
        self.canMoveUp = False
        self.canMoveDown = False

    def draw(self):
        pr.draw_sphere(self.pos, GHOST_RADIUS, self.color)

    def check_available_moves(self):
        pass
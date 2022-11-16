import pyray as pr
from map import GameState

class Menu():
    def __init__(self):
        pass

    def draw(self, gameState):
        '''Draw one of the menus'''
        if gameState == GameState.MENU:
            pr.draw_text("PACMAN 3D", 600, 300, 80, pr.DARKGREEN)
            pr.draw_text("PRESS ENTER to start", 540, 500, 50, pr.DARKGREEN)
        elif gameState == GameState.GAME_WON:
            pr.draw_text("YOU WON", 590, 300, 80, pr.DARKGREEN)
            pr.draw_text("PRESS ENTER to play again", 500, 500, 50, pr.DARKGREEN)
        elif gameState == GameState.GAME_OVER:
            pr.draw_text("GAME OVER", 580, 300, 80, pr.DARKGREEN)
            pr.draw_text("PRESS ENTER to try again", 500, 500, 50, pr.DARKGREEN)

    def update(self, gameState):
        '''Update game state'''
        if pr.is_key_pressed(pr.KEY_ENTER):
            return GameState.GAMEPLAY
        else:
            return gameState
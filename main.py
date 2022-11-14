import pyray as pr
from enum import Enum

from map import Map

class GameState(Enum):
    GAMEPLAY = 0
    PAUSED = 1
    GAME_OVER = 2
    GAME_WON = 3
    

if __name__ == '__main__':
    pr.init_window(1920, 1080, "Pacman 3D")
    pr.set_target_fps(60)

    camera = pr.Camera3D([0.0, 15.0, 10.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
    pr.set_camera_mode(camera, pr.CAMERA_PERSPECTIVE)

    map = Map()

    gameState = GameState.GAMEPLAY

    while not pr.window_should_close():
        pr.update_camera(camera)

        map.update()

        
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        pr.begin_mode_3d(camera)

        if gameState == GameState.GAMEPLAY:
            map.draw()
        elif gameState == GameState.PAUSED:
            pass #TODO
        elif gameState == GameState.GAME_WON:
            pass #TODO
        elif gameState == GameState.GAME_OVER:
            pass #TODO

        pr.end_mode_3d()
        pr.end_drawing()

    pr.close_window()
        
import pyray as pr

from map import Map, GameState
from menu import Menu
    

if __name__ == '__main__':
    pr.init_window(1600, 900, "Pacman 3D")
    pr.init_audio_device()
    pr.set_target_fps(60)

    camera = pr.Camera3D([0.0, 20.0, 15.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)

    pr.set_camera_mode(camera, pr.CAMERA_PERSPECTIVE)

    map = Map()
    menu = Menu()

    gameState = GameState.MENU

    while not pr.window_should_close():
        pr.update_camera(camera)
        if gameState == GameState.GAMEPLAY:
            gameState = map.update()
            pr.draw_text(f'Score: {map.score}', 5, 5, 40, pr.RED)
        else:
            menu.draw(gameState)
            gameState = menu.update(gameState)
            if gameState == GameState.GAMEPLAY:
                map = Map()
                continue
        
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        menu.draw(gameState)

        pr.begin_mode_3d(camera)

        if gameState == GameState.GAMEPLAY:
            map.draw()

        pr.end_mode_3d()

        pr.end_drawing()

    pr.close_window()
        
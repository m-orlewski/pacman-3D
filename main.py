import pyray as pr

from map import Map

if __name__ == '__main__':
    pr.init_window(1920, 1080, "Pacman 3D")
    pr.set_target_fps(60)

    camera = pr.Camera3D([0.0, 15.0, 10.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
    pr.set_camera_mode(camera, pr.CAMERA_PERSPECTIVE)

    map = Map()

    while not pr.window_should_close():
        pr.update_camera(camera)

        map.update()
        
        pr.begin_drawing()
        pr.clear_background(pr.RAYWHITE)
        pr.begin_mode_3d(camera)

        
        map.draw()

        pr.end_mode_3d()
        pr.end_drawing()

    pr.close_window()
        
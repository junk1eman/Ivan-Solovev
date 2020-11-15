# -*- coding: utf-8 -*-
import time
import simple_draw as sd


def sun(x, y):
    step = 0
    start_x = x // 6
    start_y = y * 5 // 6
    center_position = sd.get_point(start_x, start_y)
    radius = y // 12
    sd.circle(center_position=center_position, radius=radius, color=sd.COLOR_YELLOW, width=0)
    while step < 15:
        for _angle in range(0, 360, 15):
            ray_start = sd.get_vector(center_position, _angle + step - 3, radius)
            ray_end = sd.get_vector(ray_start.end_point, _angle + step - 3, 1.5 * radius)
            ray_end.draw(color=sd.background_color, width=5)
        for _angle in range(0, 360, 15):
            ray_start = sd.get_vector(center_position, _angle + step, radius)
            ray_end = sd.get_vector(ray_start.end_point, _angle + step, 1.5 * radius)
            ray_end.draw(color=sd.COLOR_YELLOW, width=5)
        step += 3
        time.sleep(0.05)

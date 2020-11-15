# -*- coding: utf-8 -*-
import simple_draw as sd


def land(x, y, color=(173, 119, 57)):
    x_start = 0
    y_start = 0
    start_point_home = sd.get_point(x_start, y_start)
    end_point_home = sd.get_point(x, y // 8)
    sd.rectangle(left_bottom=start_point_home, right_top=end_point_home, color=color)

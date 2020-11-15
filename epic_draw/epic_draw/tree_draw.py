# -*- coding: utf-8 -*-
import simple_draw as sd


def tree(x, y):
    x_start = 6 * x // 8
    y_start = y // 8
    start_point = sd.get_point(x_start, y_start)
    length = y // 7
    angle = 90

    def sub_tree(_point, _angle, _length):
        step_angle = 30
        v1 = sd.get_vector(start_point=_point, angle=_angle, length=_length, width=2)
        if _length < 15:
            color = sd.COLOR_GREEN
        else:
            color = (150, 75, 0)
        v1.draw(color=color)
        if _length > 5:
            k_1 = sd.random_number(-40, 20) / 100
            k_2 = sd.random_number(-20, 10) / 100
            angle_1 = _angle + (step_angle + step_angle * k_1)
            angle_2 = _angle - (step_angle + step_angle * k_1)
            _length = _length * (0.75 + 0.75 * k_2)
            sub_tree(v1.end_point, angle_1, _length)
            sub_tree(v1.end_point, angle_2, _length)

    sub_tree(start_point, angle, length)

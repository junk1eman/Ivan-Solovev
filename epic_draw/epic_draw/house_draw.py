# -*- coding: utf-8 -*-
import simple_draw as sd


def house(x, y, width=3, color=sd.COLOR_YELLOW):
    x_start = x // 5
    y_start = y // 8
    length = x // 20
    heigth = length // 3
    x_end = x_start + length * 8
    y_end = y_start + heigth * 9
    start_point_home = sd.get_point(x_start, y_start)
    end_point_home = sd.get_point(x_end, y_end)
    sd.rectangle(left_bottom=start_point_home, right_top=end_point_home, color=color, width=width)
    for x_point in range(x_start, x_end, length):
        for y_point in range(y_start, y_end, heigth * 2):
            left_bottom = sd.get_point(x_point, y_point)
            right_top = sd.get_point(x_point + length, y_point + heigth)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=width)
    for x_point in range(x_start + length // 2, x_end - length, length):
        for y_point in range(y_start + heigth, y_end, heigth * 2):
            left_bottom = sd.get_point(x_point, y_point)
            right_top = sd.get_point(x_point + length, y_point + heigth)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color, width=width)
    roof_size = x_end - x_start + 2 * heigth
    x_start_roof = x_start - heigth
    y_start_roof = y_end + 2 * width
    start_point_roof = sd.get_point(x_start_roof, y_start_roof)
    while roof_size > width:
        roof = sd.get_vector(start_point=start_point_roof, angle=0, length=roof_size)
        roof.draw(color=sd.COLOR_RED, width=width * 2)
        roof_size -= 8 * width
        x_start_roof += 4 * width
        y_start_roof += width
        start_point_roof = sd.get_point(x_start_roof, y_start_roof)

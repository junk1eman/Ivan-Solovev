# -*- coding: utf-8 -*-
import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE, sd.COLOR_RED]


def rainbow(x, y, step=10, width=10):
    for i, color in enumerate(rainbow_colors, 0):
        if i < 7:
            radius = int(x * 1.3) - step * i
            start_x = 0
            start_y = y - x
            center_position = sd.get_point(start_x, start_y)
            sd.circle(center_position=center_position, radius=radius, color=color, width=width)
            rainbow_colors[i] = rainbow_colors[i + 1]
        else:
            rainbow_colors[i] = rainbow_colors[0]
        sd.sleep(0.05)

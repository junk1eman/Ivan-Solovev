# -*- coding: utf-8 -*-
import time
import simple_draw as sd
from epic_draw import house_draw, land_draw

length_list = [14, 6, 5, 18, 10, 20, 10, 13, 13, 9]
variation = [(-13, 40), (16, 30), (-3, 2), (-2, 37), (-34, 19), (-13, 30), (-25, 35), (-3, 15), (5, 21), (14, 40)]


def man(_x, _y):
    length = 70
    color = sd.COLOR_WHITE
    width = 2

    def body(_x, _y):
        x_start = _x // 6
        y_start = _y // 7
        start_point = sd.get_point(x_start, y_start)
        body = sd.get_vector(start_point=start_point, angle=90, length=length)
        body.draw(color=color, width=width)
        leg_right = sd.get_vector(start_point=start_point, angle=-120, length=length * 2 // 3)
        leg_right.draw(color=color, width=width)
        leg_left = sd.get_vector(start_point=start_point, angle=-60, length=length * 2 // 3)
        leg_left.draw(color=color, width=width)
        start_point = sd.get_point(x_start, y_start + length // 3)
        hand_right = sd.get_vector(start_point=start_point, angle=60, length=length * 2 // 3)
        hand_right.draw(color=color)
        hand_left = sd.get_vector(start_point=start_point, angle=120, length=length * 2 // 3)
        hand_left.draw(color=color, width=width)

    def face(_x, _y, _wow=None, _color=color):
        face_radius = length // 3
        x_start = _x // 6
        y_start = _y // 7 + length + face_radius
        center_point = sd.get_point(x_start, y_start)
        sd.circle(center_position=center_point, radius=face_radius, color=_color, width=width)
        left_eye_center_point = sd.get_point(x_start - face_radius // 3, y_start + face_radius // 3)
        rigth_eye_center_point = sd.get_point(x_start + face_radius // 3, y_start + face_radius // 3)
        eye_radius = face_radius // 6
        eye_width = width // 2
        sd.circle(center_position=left_eye_center_point, radius=eye_radius, color=_color, width=eye_width)
        sd.circle(center_position=rigth_eye_center_point, radius=eye_radius, color=_color, width=eye_width)
        if _wow == 'wow':
            wow_smile_point = sd.get_point(x_start, y_start - face_radius // 3)
            sd.circle(center_position=wow_smile_point, radius=face_radius // 3, color=_color, width=eye_width)
        else:
            smile_start_point = sd.get_point(x_start - face_radius // 3, y_start - face_radius // 3)
            smile_end_point = sd.get_point(x_start + face_radius // 3, y_start - face_radius // 3)
            sd.line(start_point=smile_start_point, end_point=smile_end_point, color=_color, width=width)

    def snowfalls(_x, _y, _variation, _color=sd.COLOR_WHITE):
        snowfalls_list = []
        for _i in range(10):
            x = _x // 3 + _variation[_i][0]
            y = _y // 3 + _variation[_i][1]
            snowfalls_list.append((x, y))

        for _i, snowfall in enumerate(snowfalls_list):
            sd.snowflake(center=sd.get_point(snowfall[0], snowfall[1]), length=length_list[_i], color=_color)

    x_offset = _x
    y_offset = _y
    wow = 'wow'
    while True:
        house_draw.house(_x, _y)
        land_draw.land(_x, _y)
        body(_x, _y)
        snowfalls(_x, _y, variation)
        snowfalls(_x // 2, _y // 8, variation)
        snowfalls(x_offset, y_offset, variation, sd.background_color)
        face(_x, _y, _color=sd.background_color)
        face(_x, _y, _wow=wow, _color=sd.background_color)
        if x_offset > _x // 2:
            x_offset -= 30
            y_offset -= 9
            snowfalls(x_offset, y_offset, variation)
            face(_x, _y)
        elif y_offset > _y // 8:
            y_offset -= 30
            snowfalls(x_offset, y_offset, variation)
            face(_x, _y, wow)
        else:
            face(_x, _y, wow)
            break
        time.sleep(0.05)

# -*- coding: utf-8 -*-
from random import randint

_number = ''


def make_number():
    global _number
    _number = ''
    numb = str(randint(1, 9))
    for i in range(4):
        while numb in _number:
            numb = str(randint(0, 9))
        else:
            _number += numb
            numb = str(randint(0, 9))
    return _number


def check_number(user_number):
    _bulls_count = 0
    _cows_count = 0
    for i, sign in enumerate(user_number):
        if sign in _number:
            if sign == _number[i]:
                _bulls_count += 1
            else:
                _cows_count += 1
    return {'bulls': _bulls_count, 'cows': _cows_count}

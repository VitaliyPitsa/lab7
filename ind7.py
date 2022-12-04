#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def decorator_function(func):
    def wrapper(*args):
        res = float("{:.2f}".format(func(*args)))
        print(f"Площадь круга равна: {res} ")
        return res

    return wrapper


@decorator_function
def circle_square(r):
    return math.pi * pow(r, 2)


if __name__ == '__main__':
    circle_square(5)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def decorator_function(func):
    def wrapper(r):
        print(f"Площадь круга равна: {func(r)} ")
    return wrapper


@decorator_function
def circle_square(r):
    return round(math.pi * pow(r, 2), 2)


if __name__ == '__main__':
    circle_square(5)
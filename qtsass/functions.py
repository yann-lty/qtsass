# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015 Yann Lanthony
# Copyright (c) 2017-2018 Spyder Project Contributors
#
# Licensed under the terms of the MIT License
# (See LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Libsass functions."""

# yapf: disable

# Third party imports
import sass


# yapf: enable


def rgba(r, g, b, a):
    """Convert r,g,b,a values to standard format."""
    result = 'rgba({}, {}, {}, {}%)'
    if isinstance(r, sass.SassNumber):
        alpha = a.value if a.unit == '%' else a.value * 100
        return result.format(
            int(r.value), int(g.value), int(b.value), int(alpha))
    elif isinstance(r, float):
        return result.format(int(r), int(g), int(b), int(a * 100))


def rgba_from_color(color):
    """
    Conform rgba.

    :type color: sass.SassColor
    """
    # Inner rgba() call
    if not isinstance(color, sass.SassColor):
        return '{}'.format(color)

    return rgba(color.r, color.g, color.b, color.a)


def qlineargradient(x1, y1, x2, y2, stops):
    """
    Implement qss qlineargradient function for scss.

    :type x1: sass.SassNumber
    :type y1: sass.SassNumber
    :type x2: sass.SassNumber
    :type y2: sass.SassNumber
    :type stops: sass.SassList
    :return:
    """
    stops_str = []
    for stop in stops[0]:
        pos, color = stop[0]
        stops_str.append('stop: {} {}'.format(
            pos.value,
            rgba_from_color(color),
        ))
    template = 'qlineargradient(x1: {}, y1: {}, x2: {}, y2: {}, {})'
    return template.format(x1.value, y1.value, x2.value, y2.value,
                           ', '.join(stops_str))

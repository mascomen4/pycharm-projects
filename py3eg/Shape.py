#!/usr/bin/env python3
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This module provides the Point and Circle classes.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    # Start modification

    def __add__(self, other):
        """ Returns a sum of self and other Points

        >>> q = Point(5, 4)
        >>> r = Point(1, 3)
        >>> q + r
        Point(6, 7)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """ Return a self Point to witch added other Point

        >>> q = Point(5, 4)
        >>> r = Point(1, 3)
        >>> r += q # r = Point(6, 7)
        """
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        """ Return a subtraction of self and other Points

        >>> q = Point(5, 4)
        >>> r = Point(1, 3)
        >>> q - r
        Point(4, 1)
        """
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        """ Return a self Point from witch subtracted other Point

        >>> q = Point(5, 4)
        >>> r = Point(1, 3)
        >>> r -= q # r = Point(4, 1)
        """
        self.x *= other.x
        self.y *= other.y
        return self

    def __mul__(self, number):
        """ Multiplicate number either self item and return new Point 

        >>> q = Point(5, 4)
        >>> q*5
        Point(25, 20)
        """
        return Point(self.x*number, self.y*number)

    def __imul__(self, number):
        """ Return a self Point multiplicated by number

        >>> q = Point(5, 4)
        >>> q *= 5
        >>> q
        Point(25, 20)
        """
        self.x *= number
        self.y *= number
        return self

    def __truediv__(self, number):
        """ Return a new Point whose coord. was created by self coord. / number

        >>> q = Point(3, 6)
        >>> p = q / 3
        >>> p
        Point(1, 2)
        """
        return Point(self.x/number, self.y/number)

    def __itruediv__(self, number):
        """ Returns self Point whose coord. was created by self coord. / number

        >>> q = Point(1.5, 6)
        >>> q /= 3
        >>> q
        Point(0.5, 2)
        """
        self.x /= number
        self.y /= number
        return self

    def __floordiv__(self, number):
        """ Returns new Point whose coord. was created bu self coord. // number

        >>> q = Point(1.5, 5)
        >>> q // 3
        >>> Point(0, 1)
        """
        return Point(self.x //= number, self.y //= number)

    def __ifloordiv__(self, number):
        """ Returns self Point whose coord. was created bu self coord. // number

        >>> p = Point(4, 5)
        >>> p //= 5
        >>> p
        Point(0, 1)
        """
        self.x //= number
        self.y //= number
        return self
    
    # End modification
        

class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        """A Circle initializing

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin()
        3.0
        """
        return abs(self.distance_from_origin() - self.radius)


    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area()
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference()
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return repr(self)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod()

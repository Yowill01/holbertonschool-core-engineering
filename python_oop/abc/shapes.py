#!/usr/bin/env python3
"""Module that defines an abstract Shape class and concrete shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class that requires area and perimeter methods."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle defined by its radius."""

    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with a width and a height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any object that provides them."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

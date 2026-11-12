#!/usr/bin/env python3
"""Module that defines the Rectangle class."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits the behavior of BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle with a validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

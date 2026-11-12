#!/usr/bin/env python3
"""Module that defines the Square class with string output."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square, a specialized rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)

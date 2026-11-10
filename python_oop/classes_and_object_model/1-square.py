#!/usr/bin/env python3
"""Module that defines a Square class with a private size."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the square (stored privately).
        """
        self.__size = size

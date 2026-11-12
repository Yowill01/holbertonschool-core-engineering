#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception: area is not implemented in this class."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name (str): name of the value, used in error messages.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

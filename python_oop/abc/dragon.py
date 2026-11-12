#!/usr/bin/env python3
"""Module that defines mixins and a Dragon class that combines them."""


class SwimMixin:
    """Mixin that adds the ability to swim."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds the ability to fly."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon that can swim, fly and roar."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")

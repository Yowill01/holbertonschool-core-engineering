#!/usr/bin/env python3
"""Module that defines Fish, Bird and FlyingFish with multiple inheritance."""


class Fish:
    """Fish that lives in water."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    """Bird that lives in the sky."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Flying fish that combines the behavior of Fish and Bird."""

    def fly(self):
        """Print that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")

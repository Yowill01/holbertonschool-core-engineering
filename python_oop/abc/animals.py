#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that requires a sound method."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog, a concrete animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat, a concrete animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"

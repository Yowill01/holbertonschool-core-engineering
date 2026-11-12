#!/usr/bin/env python3
"""Module that defines VerboseList, a list that reports its changes."""


class VerboseList(list):
    """List that prints a message when items are added or removed."""

    def append(self, item):
        """Add an item to the list and print a message."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Print a message and remove the item from the list."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Print a message and pop the item at the given index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)

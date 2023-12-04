"""File to define Fish class."""

__author__ = "730702719"


class Fish:
    """Creates a new class fish."""
    age: int
    
    def __init__(self, init_age: int = 0):
        """Intializes a fish with an age value."""
        self.age = init_age
    
    def one_day(self):
        """Age increases by one after a day."""
        self.age += 1
        return None
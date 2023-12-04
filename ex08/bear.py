"""File to define Bear class."""

__author__ = "730702719"


class Bear:
    """Creates a new bear class."""
    age: int
    hunger_score: int
    
    def __init__(self, age_init: int = 0, hunger_score: int = 0):
        """Create a bear with an age and hunger score."""
        self.age = age_init
        self.hunger_score = hunger_score
    
    def one_day(self):
        """Age increasing by 1 and Hunger Score decreasing by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """When a bear eats a fish his hunger score goes up by 1."""
        self.hunger_score += num_fish
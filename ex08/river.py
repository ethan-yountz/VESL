"""File to define River class."""

__author__ = "730702719"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """New Class River."""
    day: int
    fish: list()
    bears: list()
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of bears and fish to see who will survive."""
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []
        for individual in self.fish:
            if individual.age <= 3:
                surviving_fish.append(individual)
        for individual in self.bears:
            if individual.age <= 5:
                surviving_bears.append(individual)
        self.fish = surviving_fish
        self.bears = surviving_bears

    def remove_fish(self, amount: int):
        """Remove a certain amount of fish."""
        for x in range(0, amount):
            self.fish.pop(0) 

    def bears_eating(self):
        """Bears Eat 3 fish if there is enough alive."""
        for individual in self.bears:
            if len(self.fish) >= 5:
                individual.eat(3)
                self.remove_fish(3)
        return None
    
    def check_hunger(self):
        """Checks hunger of bears and kills them off."""
        surviving_bears: list[Bear] = []
        for individual in self.bears:
            if individual.hunger_score >= 0:
                surviving_bears.append(individual)
        self.bears = surviving_bears
        
    def repopulate_fish(self):
        """Repopulating fish based on equation."""
        num_offspring: int = (len(self.fish) // 2) * 4
        for x in range(0, num_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulating bears based on equation."""
        num_offspring: int = len(self.bears) // 2
        for x in range(0, num_offspring):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Way to view river using f-string."""
        print(f"~~~ Day {self.day}: ~~~\nFish Population: {len(self.fish)}\nBear Population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
    
    def one_river_week(self):
        """Rins one day 7 times."""
        for x in range(0, 7):
            self.one_river_day()
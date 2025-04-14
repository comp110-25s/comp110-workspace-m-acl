"""File to define River class."""

__author__: str = "730641475"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear

# for local testing
# from fish import Fish
# from bear import Bear


class River:
    """I AM THE EMBODIMENT OF RIVER WOOSH!"""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Oldies die :(."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for fishboi in self.fish:
            # less than lives
            if fishboi.age <= 3:
                new_fish.append(fishboi)

        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)

        self.fish = new_fish
        self.bears = new_bears

        return None

    def remove_fish(self, amount: int) -> None:
        """First fish go bye bye."""
        for f_idx in range(0, amount):
            self.fish.pop(f_idx)

        return None

    def bears_eating(self):
        """Bear go chomp da fishies."""
        # doing >=5 check as fish wont increase in the eating process
        # this way if num fish left is < 5 we just skip over looping the bears
        if len(self.fish) >= 5:
            for bear in self.bears:
                if len(self.fish) >= 5:
                    bear.eat(3)
                    self.remove_fish(3)

        return None

    def check_hunger(self):
        """Checks if bears die from hunger."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)

        self.bears = new_bears
        return None

    def repopulate_fish(self):
        """Fish always have quartlets."""
        num_babies = (len(self.fish) // 2) * 4

        for _ in range(0, num_babies):
            self.fish.append(Fish())

        return None

    def repopulate_bears(self):
        """Just one kid is a BEAR already."""
        num_babies = len(self.bears) // 2

        for _ in range(0, num_babies):
            self.bears.append(Bear())

        return None

    def view_river(self) -> None:
        """Gives summary of river."""
        print(f"~~~ Day {self.day}: ~~~\n")
        print(f"Fish population: {len(self.fish)}\n")
        print(f"Bear population: {len(self.bears)}\n")
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

    def one_river_week(self) -> None:
        """One week in the life of a river."""
        for _ in range(0, 7):
            self.one_river_day()

        return None

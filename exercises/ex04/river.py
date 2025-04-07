"""File to define River class."""

# import bear
# import fish
# class River:
#     day: int
#     bears: list[bear.Bear]
#     fishes: list[fish.Fish]

#     def __init__(self, num_bears: int, num_fish: int) -> None:
#         self.day = 0
#         self.bears = []
#         self.fish = []

#       # the type-ignore is just to get rid of the warnign that I never use x inside it
#       # x is just for looping, does not need to be accessed inside the loop
#         for x in range(num_fish):  # type: ignore
#             self.fish.append(fish.Fish())

#         for x in range(num_bears):  # type: ignore
#             self.bears.append(bear.Bear())


from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        return None

    def bears_eating(self):
        return None

    def check_hunger(self):
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
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

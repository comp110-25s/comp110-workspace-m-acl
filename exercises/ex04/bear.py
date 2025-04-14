"""File to define Bear class."""

__author__: str = "730641475"


class Bear:
    """Tis a bear yo."""

    age: int
    hunger_score: int

    def __init__(self):
        """Bearo is borno."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """A day in the life of a bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Bear go yummy!"""
        self.hunger_score += num_fish
        return None

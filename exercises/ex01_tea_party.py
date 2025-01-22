"""Exercise 01 Tea Party - uses guests, get supplies needed + cost"""

__author__: str = "730641475"


def main_planner(guests: int) -> None:
    """Prints total tea bags + treats need, as well as total cost"""

    print("A Cozy Tea Party for " + str(guests) + " People :D")

    print("Tea Bags: " + str(tea_bags(people=guests)))

    print("Treats: " + str(treats(people=guests)))

    print("Cost: $" + str(cost(tea_count=tea_bags(guests), treat_count=treats(guests))))


def tea_bags(people: int) -> int:
    """This calcs the number of teabags per attendee"""

    return people * 2


def treats(people: int) -> int:
    """Calcs the num of treats per tea had"""

    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calcs total cost of both teabags + treats"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

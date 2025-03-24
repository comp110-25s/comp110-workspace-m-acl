"""Ex03 main file"""

__author__: str = "730641475"


def invert(input: dict[str, str]) -> dict[str, str]:
    """inverts a dictionary's keys and values. Raises Errors as needed"""
    output: dict[str, str] = {}

    for key in input:
        new_key: str = input[key]
        new_val: str = key

        if new_key not in output:
            output[new_key] = new_val

        else:
            raise KeyError("you cannot have duplicate keys. Check for duplicate values")
    return output


print(invert({"hi": "how_ymou", "bye": "how_you", "wha": "nvm"}))


def count(input: list[str]) -> dict[str, int]:
    """Returns dictionary counting number of times x occurs in a list."""
    # returns as x:#times

    output: dict[str, int] = {}

    for list_i in input:
        if list_i in output:
            output[list_i] += 1

        else:
            output[list_i] = 1

    return output


print(
    count(
        [
            "john",
            "john",
            "jarnATHAN",
            "me",
            "john",
            "monsieur peanut butter",
            "me",
            "JARNATHAN",
        ]
    )
)


def favorite_color(people_fav: dict[str, str]) -> str:
    colors: list[str] = []

    for person in people_fav:
        colors.append(people_fav[person])

    return "hi"

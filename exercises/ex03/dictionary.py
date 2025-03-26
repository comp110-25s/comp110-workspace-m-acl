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


def favorite_color(people_fav: dict[str, str]) -> str:
    """Gets everyone's favorite color and returns most popular"""
    colors: list[str] = []

    for person in people_fav:
        colors.append(people_fav[person])

    best_col: str = ""
    max_vote: int = 0
    for color in count(colors):
        if count(colors)[color] > max_vote:
            best_col = color
            max_vote = count(colors)[color]

    return best_col


def bin_len(listo: list[str]) -> dict[int, set[str]]:
    """takes list of strings and returns grouped by word length"""
    bins: dict[int, set[str]] = {}

    for word in listo:

        if not len(word) in bins:
            bins[len(word)] = {word}

        else:
            bins[len(word)].add(word)

    return bins

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
    output: dict[str, int] = {}

    for key in input:
        if key in input:
            output[key] += 1

        else:
            output[key] = 1

    return output

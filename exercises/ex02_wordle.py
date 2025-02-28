"""Exercise 02 Wordle game"""

__author__: str = "730641475"


def contains_char(word: str, char: str) -> bool:
    """checks if given char is in word"""
    assert len(char) == 1, f"len('{char}') is not 1"

    i: int = 0
    while i < len(word):

        if word[i] == char:
            return True

        i += 1
    return False


print(contains_char("dog", "o"))

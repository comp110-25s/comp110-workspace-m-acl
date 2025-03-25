"""Ex03 test file"""

__author__: str = "730641475"

# import pytest

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert() -> None:
    assert True

    assert invert({"hi": "how_ymou", "bye": "how_you", "wha": "nvm"}) == {
        "how_ymou": "hi",
        "how_you": "bye",
        "nvm": "wha",
    }


def test_count() -> None:
    assert True

    assert count(
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
    ) == {
        "john": 3,
        "jarnATHAN": 1,
        "me": 2,
        "monsieur peanut butter": 1,
        "JARNATHAN": 1,
    }


def test_favorite_color() -> None:
    assert True

    assert favorite_color(
        {
            "john": "purple",
            "micah": "yellow",
            "heyzzues": "yellow",
            "athena": "blue",
            "grumbus": "purple",
            "jaranathan": "yellow",
        }
    ) == {
        4: {"blue", "john"},
        6: {"purple", "yellow", "athena"},
        5: {"micah"},
        8: {"heyzzues"},
        7: {"grumbus"},
        10: {"jaranathan"},
    }


def test_bin_len() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


# Also inside the exercises/ex03 directory, create a file named dictionary_test.py. Add
# a docstring and establish an __author__ in this file as well.

# For each function from below (invert, count, favorite_color, bin_len), you are to
#
#  define at least 3x unit test functions. Remember that a unit test function
# starts with test_.

# The 3 unit tests should consist of:

# One edge case
# Two use cases
# Include descriptive function names and docstrings, so that it captures
#  what is being tested.

# python -m pytest exercises/ex03

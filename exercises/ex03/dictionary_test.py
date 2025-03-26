"""Ex03 test file"""

__author__: str = "730641475"

import pytest  # when i want to test for error


# The 3 unit tests should consist of:

# One edge case
# Two use cases

# python -m pytest exercises/ex03

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_multi_kp() -> None:
    """Use case for multiple key-value pairs"""
    assert invert({"hi": "how_ymou", "bye": "how_you", "wha": "nvm"}) == {
        "how_ymou": "hi",
        "how_you": "bye",
        "nvm": "wha",
    }


def test_invert_use_single_kp() -> None:
    """use case for if only one key-pair value"""

    # single key-value pair
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_edge_empty() -> None:
    """Checks if empty dictionary returns empty dict"""
    assert invert({}) == {}


def test_invert_edge_keyerror() -> None:
    """Checks if multiple identical values in dict, raises KeyError"""
    # b/c values --> keys, keys must be unique
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_count_use_multi() -> None:
    """Checks that list of multiple returns count"""

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


def test_count_use_only_one() -> None:
    """Checks that list of just 1 string returns dict with 1 k-p"""
    assert count(
        [
            "john",
            "john",
            "john",
            "john",
        ]
    ) == {"john": 4}


def test_count_edge_empty() -> None:
    """Checks that if input empty list, get an empty dictionary"""
    assert count([]) == {}


def test_favorite_color_use_1() -> None:

    assert (
        favorite_color(
            {
                "john": "purple",
                "micah": "yellow",
                "heyzzues": "yellow",
                "athena": "blue",
                "grumbus": "purple",
                "jaranathan": "yellow",
            }
        )
        == "yellow"
    )


def test_favorite_color_use_2() -> None:

    assert (
        favorite_color(
            {
                "john": "purple",
                "micah": "yellow",
                "heyzzues": "yellow",
                "athena": "blue",
                "grumbus": "purple",
                "jaranathan": "yellow",
            }
        )
        == "yellow"
    )


def test_favorite_color_edge() -> None:
    """Checks that empty dict returns empty str"""

    assert favorite_color({}) == ""


def test_bin_len() -> None:

    assert bin_len(
        [
            "john",
            "purple",
            "micah",
            "yellow",
            "heyzzues",
            "yellow",
            "athena",
            "blue",
            "grumbus",
            "purple",
            "jaranathan",
            "yellow",
        ]
    ) == {
        4: {"blue", "john"},
        6: {"purple", "yellow", "athena"},
        5: {"micah"},
        8: {"heyzzues"},
        7: {"grumbus"},
        10: {"jaranathan"},
    }

    # just adding these - should be testing for the same use case
    # if this test fails, can separate along this line into multiple tests
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

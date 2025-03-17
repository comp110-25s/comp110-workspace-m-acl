"""testing teh dummy file you dummy"""

from dummy_file import count_regs, wazzup


def test_count_regs_use_1() -> None:
    """testing use case 1"""
    assert count_regs("Orange", ["Orange", "Durham", "Orange", "Chatham"]) == 2


def test_wazzup() -> None:
    """testing wazzup func"""
    assert wazzup() == -1


def test_count_regs_empty() -> None:
    """testing edge case empty list"""
    assert count_regs("Orange", []) == 0


def test_count_regs_side_effects() -> None:
    countys: list[str] = ["Orange", "Durham", "Orange", "Chatham"]

    count_regs("Orange", countys)

    assert countys == ["Orange", "Durham", "Orange", "Chatham"]

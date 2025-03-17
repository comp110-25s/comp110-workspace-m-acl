"""the dummy line to test"""


def count_regs(coi: str, counties: list[str]) -> int:
    """Count number of people who are registered in the
    specified county."""
    idx: int = 0  # Current index in counties list
    total: int = 0  # Total occurrences of county of interest

    while idx < len(counties):
        if counties[idx] == coi:
            total += 1

        idx += 1

    # to make the side_effects test fail
    # counties.append("hi")
    return total


def wazzup() -> int:
    return -1

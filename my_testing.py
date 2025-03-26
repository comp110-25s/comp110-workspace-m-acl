def pack(df: float) -> str:
    """Packing advice"""

    if df >= 75.0:
        return "short sleeves"

    else:
        if df <= 50.0:
            if df <= 0.0:
                return "stay inside"

            else:  # if 0 <= df < 50
                return "long sleeves"

    return "idk this aint clear"


print(pack(60))


def group_names(names: list[str]) -> dict[str, int]:
    groups: dict[str, int] = {}
    first_letter: str
    for n in names:
        first_letter = n[0]
        if first_letter in groups:
            groups[first_letter] += 1

        else:
            groups[first_letter] = 1

    return groups


ppl: list[str] = ["Karen", "Emily", "Kris"]
output: dict[str, int] = group_names(names=ppl)

print(output)

output["I"] = 1
print(output)

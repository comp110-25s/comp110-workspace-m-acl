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

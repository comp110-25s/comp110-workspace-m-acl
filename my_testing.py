# def pack(df: float) -> str:
#     """Packing advice"""

#     if df >= 75.0:
#         return "short sleeves"

#     else:
#         if df <= 50.0:
#             if df <= 0.0:
#                 return "stay inside"

#             else:  # if 0 <= df < 50
#                 return "long sleeves"

#     return "idk this aint clear"


# # print(pack(60))


# def group_names(names: list[str]) -> dict[str, int]:
#     groups: dict[str, int] = {}
#     first_letter: str
#     for n in names:
#         first_letter = n[0]
#         if first_letter in groups:
#             groups[first_letter] += 1

#         else:
#             groups[first_letter] = 1

#     return groups


# ppl: list[str] = ["Karen", "Emily", "Kris"]
# output: dict[str, int] = group_names(names=ppl)

# # print(output)

# output["I"] = 1
# # print(output)


# class Profile:
#     username: str

#     def __init__(self):
#         self.username = "hi"
#         self.am_cool = True


# prof: Profile = Profile()
# print(prof.am_cool)


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def dist_from_origin(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def translate_x(self, dx: float) -> None:
        self.x += dx

    def translate_y(self, dy: float) -> None:
        self.y += dy


pt: Point = Point(2.0, 1.0)
print(pt.dist_from_origin())
pt.translate_y(1)
print(pt.dist_from_origin())

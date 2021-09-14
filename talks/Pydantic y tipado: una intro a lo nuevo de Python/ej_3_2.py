from dataclasses import dataclass


@dataclass
class TomHanks():
    name: str
    age: int
    profession: str


tom_hanks_1 = TomHanks("Forest Gump", 26, "Several")
tom_hanks_2 = TomHanks("Jim Lovell", 37, "Astronaut")
tom_hanks_3 = TomHanks("Chuck Noland", 34, "Fedex Engineer")

print(tom_hanks_1)
print(tom_hanks_2)
print(tom_hanks_3)

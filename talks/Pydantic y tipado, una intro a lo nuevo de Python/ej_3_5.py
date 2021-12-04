from typing import List, Optional
from pydantic import BaseModel, validator
import json
import pprint
import enum


class Strength(enum.Enum):
    RUNS = "Runs fast"
    BRAVE = "Brave"
    MAKES_FIRE = "Makes fire"


class TomHanks(BaseModel):
    name: str
    age: int
    profession: str
    strength: Optional[Strength]

    @validator("age")
    def age_el_to_40(cls, value):
        if not value <= 40:
            raise ValueError("Age must be equal lower to 40.")
        return value


def main() -> List[TomHanks]:
    with open("./tom_hanks_2.json") as file:
        data = json.load(file)
        tom_hanks: List[TomHanks] = [TomHanks(**tom) for tom in data]
    return tom_hanks


pp = pprint.PrettyPrinter(indent=2)
data = main()
pp.pprint(data)

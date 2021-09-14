from typing import List, Optional
from pydantic import BaseModel, validator
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


tom = TomHanks(
    name="John H. Miller",
    age=34,
    profession="Soldier",
    strength=Strength.BRAVE
)

# tom = TomHanks(
#     **{
#         "name": "John H. Miller",
#         "age": 34,
#         "profession": "Soldier",
#         "strength":Strength.BRAVE
#     }
# )

# tom = TomHanks.parse_obj(
#     {
#         "name": "John H. Miller",
#         "age": 34,
#         "profession": "Soldier",
#         "strength":Strength.BRAVE
#     }
# )

# tom = TomHanks.parse_raw(
#     '{\
#         "name": "John H. Miller",\
#         "age": 34,\
#         "profession": "Soldier",\
#         "strength": "Brave"\
#     }'
# )

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(tom)
# pp.pprint(tom.dict())
# pp.pprint(tom.json())
# pp.pprint(tom.schema())

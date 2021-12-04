from typing import List, Optional
from pydantic import BaseModel
import json
import pprint


class TomHanks(BaseModel):
    name: str
    age: int
    profession: str


def main() -> List[TomHanks]:
    with open("./tom_hanks_1.json") as file:
        data = json.load(file)
        tom_hanks: List[TomHanks] = [TomHanks(**tom) for tom in data]
    return tom_hanks


pp = pprint.PrettyPrinter(indent=2)
data = main()
pp.pprint(data)

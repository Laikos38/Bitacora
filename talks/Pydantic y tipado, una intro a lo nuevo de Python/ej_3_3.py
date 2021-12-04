from pydantic import BaseModel


class TomHanks(BaseModel):
    name: str
    age: int
    profession: str


tom_hanks_1 = TomHanks(name="Forest Gump", age=26, profession="Several")
tom_hanks_2 = TomHanks(name="Jim Lovell", age=37, profession="Astronaut")
tom_hanks_3 = TomHanks(name="Chuck Noland", age=34, profession="Fedex Engineer")

print(tom_hanks_1)
print(tom_hanks_2)
print(tom_hanks_3)

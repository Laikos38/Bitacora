class TomHanks():
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession
    
    def __repr__(self):
        return f"{self.name}, {self.age}, {self.profession}"


tom_hanks_1 = TomHanks("Forest Gump", 26, "Several")
tom_hanks_2 = TomHanks("Jim Lovell", 37, "Astronaut")
tom_hanks_3 = TomHanks("Chuck Noland", 37, "Fedex Engineer")

print(tom_hanks_1)
print(tom_hanks_2)
print(tom_hanks_3)

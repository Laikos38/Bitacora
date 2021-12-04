from typing import Iterable


class Material:
    name: str
    quantity: int

    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

def print_materials(materials: Iterable[Material]) -> None:
    for m in materials:
        print(f"Material: {m.name} ; Quantity: {m.quantity}")


print("----- Dentist tool:")
materials_tool = [Material("ice skate", 1), Material("coconut", 1), Material("tooth", 1)]
print_materials(materials_tool)
materials_spear = (Material("vhs tape", 3), Material("sharp rock", 1), Material("stick", 1))
print("----- Spear:")
print_materials(materials_spear)

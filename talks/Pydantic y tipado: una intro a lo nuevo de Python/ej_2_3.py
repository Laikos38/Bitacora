from typing import Iterable, Tuple


Material = Tuple[str, int]  # Alias

def print_materials(materials: Iterable[Material]) -> None:
    for m, q in materials:
        print(f"Material: {m} ; Quantity: {q}")


print("----- Dentist tool:")
materials_tool = [("ice skate", 1), ("coconut", 1), ("tooth", 1)]
print_materials(materials_tool)
materials_spear = (("vhs tape", 3), ("sharp rock", 1), ("stick", 1))
print("----- Spear:")
print_materials(materials_spear)

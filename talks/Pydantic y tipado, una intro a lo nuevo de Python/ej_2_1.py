def print_materials(materials) -> None:
    for m, q in materials:
        print(f"Material: {m} ; Quantity: {q}")


print("----- Dentist tool:")
materials = [("ice skate", 1), ("coconut", 1), ("tooth", 1)]
print_materials(materials)

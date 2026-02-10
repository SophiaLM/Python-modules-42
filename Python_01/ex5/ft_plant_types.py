#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter


class Vegetable(Plant):
    def __init__(self, name, height, age, hearvest_season):
        super().__init__(name, height, age)
        self.hearvest_season = hearvest_season


print("=== Garden Plant Types ===\n")

Rose = Flower("Rose", 25, 30, "red")
Oak = Tree("Tree", 500, 1825, 50)
Tomato = Vegetable("Tomato", 80, 90, "summer")

print(
    f"{Rose.name} (Flower): {Rose.height}cm, "
    f"{Rose.age} days, {Rose.color} color\n"
    f"Rose is blooming beautifully!\n"
    )

print(
    f"{Oak.name} (Flower): {Oak.height}cm, "
    f"{Oak.age} days, {Oak.trunk_diameter} diameter\n"
    f"Oak provides 78 square meters of shade\n"
    )

print(
    f"{Tomato.name} (Flower): {Tomato.height}cm, "
    f"{Tomato.age} days, {Tomato.hearvest_season} hearvest\n"
    f"Tomato is rich in vitamin C"
    )

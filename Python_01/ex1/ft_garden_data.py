#!/usr/bin/env python3

print("=== Garden Plant Registry ===")


class Plants:
    def __init__(self, plant, height, day):
        self.plant = plant
        self.height = height
        self.day = day


flower1 = Plants("Rose", 25, 30)
flower2 = Plants("Sunflower", 80, 45)
flower3 = Plants("Cactus", 15, 120)

garden = [flower1, flower2, flower3]
for plant in garden:
    print(f"{plant.plant}: {plant.height}cm, {plant.day} days old")

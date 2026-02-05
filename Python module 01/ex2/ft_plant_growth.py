#!/usr/bin/env python3

class Plants:
    def __init__(self, name, height, day):
        self.name = name
        self.height = height
        self.day = day


count = 1
Rose = Plants("Rose", 25, 30)
print(f"=== Day {count} ===")
print(f"{Rose.name}: {Rose.height}cm, {Rose.day} days old")
while count < 7:
    Rose.height += 1
    Rose.day += 1
    count += 1
print(f"=== Day {count} ===")
print(f"{Rose.name}: {Rose.height}cm, {Rose.day} days old")
print(f"Growth this week: +{count - 1}cm")

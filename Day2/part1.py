#!/bin/env python

with open("input.txt") as f:
    lines = f.readlines()

horizontal = 0
depth = 0
for line in lines:
    [cmd, units] = line.split(" ")
    if cmd == "forward":
        horizontal += int(units)
    elif cmd == "down":
        depth += int(units)
    elif cmd == "up":
        depth -= int(units)

print("Horizontal:", horizontal)
print("Depth:", depth)
print("Product:", horizontal * depth)
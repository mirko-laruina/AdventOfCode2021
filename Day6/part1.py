#!/bin/env python3

with open("input.txt") as f:
    line = f.readline()
    fish = [ int(i) for i in line.strip().split(",")]

for i in range(80):
    nextFish = []
    for a_fish in fish:
        if a_fish > 0:
            nextFish.append(a_fish - 1)
        else:
            nextFish.append(6)
            nextFish.append(8)
    
    fish = nextFish
    print(f"After {i + 1} day(s): {len(fish)} fish")

print("Total:", len(fish))
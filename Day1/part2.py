#!/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

previous_value = -1
count = 0

for i in range(3, len(lines)):
    if(int(lines[i]) > int(lines[i-3])):
        count += 1

print(count)
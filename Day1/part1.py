#!/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

previous_value = -1
count = -1 # since the first measurement should not be taken into consideration
for line in lines:
    current_value = int(line)
    if(current_value > previous_value):
        count += 1
    previous_value = current_value

print(count)
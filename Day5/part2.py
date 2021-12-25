#!/bin/env python3
import numpy as np
import sys

with open("input.txt") as f:
    lines = f.readlines()


couples = []
max_x = 0
max_y = 0
for line in lines:
    [start, end] = line.strip().split("->")
    start = [int(s) for s in start.split(",")]
    end = [int(s) for s in end.split(",")]

    if start[0] > max_x : max_x = start[0]
    if start[1] > max_y : max_y = start[1]
    if end[0] > max_x : max_x = end[0]
    if end[1] > max_y : max_y = end[1]
    couples.append([start, end])

ocean_map = np.zeros((max_x + 1, max_y + 1))

for couple in couples:
    start = couple[0]
    end = couple[1]

    
    step_x = 0 if end[0] == start[0] else (1 if end[0] - start[0] > 0 else -1)
    step_y = 0 if end[1] == start[1] else (1 if end[1] - start[1] > 0 else -1)

    step = (step_x, step_y)

    current = start
    while not (current[0] == end[0] and current[1] == end[1]):
        ocean_map[current[0]][current[1]] += 1
        current[0] += step[0]
        current[1] += step[1]
    ocean_map[end[0]][end[1]] += 1


print(ocean_map)
print(np.count_nonzero(ocean_map >= 2))
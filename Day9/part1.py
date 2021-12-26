#!/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

cave_map = []
for line in lines:
    cave_map.append([int(i) for i in list(line.strip())])

local_mins = []

map_heigth = len(cave_map)
map_width = len(cave_map[0])
for i in range(map_heigth):
    for j in range(map_width):
        if i > 0 and cave_map[i][j] >= cave_map[i-1][j]: continue
        if i < map_heigth - 1 and cave_map[i][j] >= cave_map[i+1][j]: continue
        if j > 0 and cave_map[i][j] >= cave_map[i][j-1]: continue
        if j < map_width - 1 and cave_map[i][j] >= cave_map[i][j+1]: continue

        local_mins.append(cave_map[i][j])

print(local_mins)
print("Risk level:", sum(local_mins) + len(local_mins))
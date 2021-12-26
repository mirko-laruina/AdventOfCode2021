#!/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

cave_map = []
for line in lines:
    cave_map.append([[int(i), -1] for i in list(line.strip())])

basins = []
counter = 0
map_heigth = len(cave_map)
map_width = len(cave_map[0])
for i in range(map_heigth):
    current_basin = None
    for j in range(map_width):
        if cave_map[i][j][0] == 9:
            current_basin = None
            continue

        if current_basin == None:
            # we could be at the beginning of a row or after a 9
            if i > 0 and cave_map[i-1][j][0] != 9:
                    current_basin = cave_map[i-1][j][1]

            else:
                current_basin = [ counter, [] ]
                counter += 1
                basins.append(current_basin)
        else:
            # we could merge two basins in one
            if i > 0 and cave_map[i-1][j][0] != 9 and current_basin != cave_map[i-1][j][1]:
                other_basin = cave_map[i-1][j][1]
                # print(f"i: {i}, j:{j}")
                # print("Basins:", basins)
                # print("Other basin:", other_basin)
                # print("Basin to remove:", current_basin)
                basins.remove(current_basin)
                for point in current_basin[1]:
                    point[1] = other_basin
                other_basin[1] += current_basin[1]
                current_basin = other_basin

        cave_map[i][j][1] = current_basin
        current_basin[1].append(cave_map[i][j])


basins = sorted(basins, key=lambda x: -len(x[1]))
product = 1
for i in range(3):
    product *= len(basins[i][1])

print("Top 3 basins product:", product)
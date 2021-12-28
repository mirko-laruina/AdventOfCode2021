#!/bin/env python3

# Dijkstra algo using basic Python data structures + heap
# It could be improved quite a lot
# Running time ~3s for part2

import heapq

class Location:
    distance = -1
    predecessor = None

    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

    def __lt__(self, other):
        return self.distance < other.distance

def compute_node_distance(starting_location, target_location, border_nodes):
    possible_distance = starting_location.distance + target_location.cost
    if target_location.distance == -1 or target_location.distance > possible_distance:
        target_location.distance = possible_distance
        target_location.predecessor = starting_location
        heapq.heappush(border_nodes, target_location)
        #border_nodes.append(target_location)

def generate_bigger_map(map, multiplier):
    row_num = len(map)
    col_num = len(map[0])
    bigger_map_x = []
    for row in map:
        bigger_row = []
        for duplicate_num in range(multiplier):
            for i, loc in enumerate(row):
                cost = (loc.cost - 1 + duplicate_num) % 9 + 1
                bigger_row.append(Location(loc.x + duplicate_num * col_num, loc.y, cost))
        bigger_map_x.append(bigger_row)

    bigger_map = []
    for i in range(multiplier):
        for row in bigger_map_x:
            bigger_map.append([Location(loc.x, loc.y + i * row_num, (loc.cost - 1 + i) % 9 + 1) for loc in row])

    return bigger_map

with open("input.txt") as f:
    lines = f.readlines()


locations = []
for i, line in enumerate(lines):
    line = line.strip()
    row = []
    locations.append(row)
    for j, char in enumerate(line):
        row.append(Location(j, i, int(char)))

row_num = len(locations)
col_num = len(locations[0])

BIGGER_MUL = 5

locations = generate_bigger_map(locations, BIGGER_MUL)
row_num = row_num * BIGGER_MUL
col_num = col_num * BIGGER_MUL

locations[0][0].distance = 0

target_location = locations[-1][-1]
border_nodes = [locations[0][0]]

while target_location.distance == -1:
    min_dist_location = heapq.heappop(border_nodes)

    if min_dist_location.y < row_num - 1:
        bottom_location = locations[min_dist_location.y + 1][min_dist_location.x]
        compute_node_distance(min_dist_location, bottom_location, border_nodes)

    if min_dist_location.y > 0:
        top_location = locations[min_dist_location.y - 1][min_dist_location.x]
        compute_node_distance(min_dist_location, top_location, border_nodes)
    
    if min_dist_location.x > 0:
        left_location = locations[min_dist_location.y][min_dist_location.x - 1]
        compute_node_distance(min_dist_location, left_location, border_nodes)

    if min_dist_location.x < col_num - 1:
        right_location = locations[min_dist_location.y][min_dist_location.x + 1]
        compute_node_distance(min_dist_location, right_location, border_nodes)

print("Distance to reach end:", target_location.distance)
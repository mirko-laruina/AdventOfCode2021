#!/bin/env python3

class Location:
    distance = -1
    predecessor = None

    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost

def compute_node_distance(starting_location, target_location, border_nodes):
    possible_distance = starting_location.distance + target_location.cost
    if target_location.distance == -1 or target_location.distance > possible_distance:
        target_location.distance = possible_distance
        target_location.predecessor = starting_location
        border_nodes.append(target_location)

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

locations[0][0].distance = 0

target_location = locations[-1][-1]
border_nodes = [locations[0][0]]
while target_location.distance == -1:
    sorted_nodes = sorted(border_nodes, key=lambda l: l.distance)
    # for node in sorted_nodes:
    #     print(node.x, node.y, node.cost, node.distance)
    # print()
    min_dist_location = sorted_nodes[0]
    border_nodes.remove(min_dist_location)

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
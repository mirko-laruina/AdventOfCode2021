#!/bin/env python3

def get_path_count_from_node(neighbours, node, visited_nodes, double_visit):
    if node == 'end':
        return 1

    if node == 'start' and len(visited_nodes) > 0:
        return 0

    if node.islower() and node in visited_nodes:
        if double_visit:
            return 0
        double_visit = True

    visited = visited_nodes.copy()
    visited.append(node)
    count = 0
    for neigh in neighbours[node]:
        count += get_path_count_from_node(neighbours, neigh, visited, double_visit)
    return count


with open("input.txt") as f:
    lines = f.readlines()


neighbours = {}

    

for line in lines:
    item1, item2 = line.strip().split("-")

    if item1 not in neighbours:
        neighbours[item1] = []
    neighbours[item1].append(item2)

    if item2 not in neighbours:
        neighbours[item2] = []
    neighbours[item2].append(item1)

paths = get_path_count_from_node(neighbours, 'start', [], False)
print("Total paths:", paths)

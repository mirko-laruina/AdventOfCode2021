#!/bin/env python3

def get_path_count_from_node(neighbours, node, visited_nodes):
    if node == 'end':
        return 1

    if node.islower() and node in visited_nodes:
        return 0


    visited = visited_nodes.copy()
    visited.append(node)
    count = 0
    for neigh in neighbours[node]:
        count += get_path_count_from_node(neighbours, neigh, visited)
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

paths = get_path_count_from_node(neighbours, 'start', [])
print("Total paths:", paths)

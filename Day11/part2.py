#!/bin/env python3

def propagate(matrix, i, j):
    if i > 0:
        check_and_flash(matrix, i-1, j)
        if j > 0:
            check_and_flash(matrix, i-1, j-1)
        if j < len(matrix[0]) - 1:
            check_and_flash(matrix, i-1, j+1)
    
    if i < len(matrix) - 1:
        check_and_flash(matrix, i+1, j)
        if j > 0:
            check_and_flash(matrix, i+1, j-1)
        if j < len(matrix[0]) - 1:
            check_and_flash(matrix, i+1, j+1)

    if j > 0:
        check_and_flash(matrix, i, j-1)
    
    if j < len(matrix) - 1:
        check_and_flash(matrix, i, j+1)


def check_and_flash(matrix, i, j):
    if matrix[i][j] == -1:
        return

    matrix[i][j] += 1
    if matrix[i][j] > 9:
        # print(f"Flash {i} {j}")
        matrix[i][j] = -1
        propagate(matrix, i, j)


def pretty_print(matrix):
    for row in matrix:
        print(row)

with open("input.txt") as f:
    lines = f.readlines()

octo_map = []
for line in lines:
    octo_map.append([int(c) for c in list(line.strip())])


step = 0
while True:
    step += 1
    for i, _ in enumerate(octo_map):
        for j, _ in enumerate(octo_map[i]):
            check_and_flash(octo_map, i, j)


    all_flashing = True
    for i, _ in enumerate(octo_map):
        for j, _ in enumerate(octo_map[i]):
            if octo_map[i][j] == -1:
                octo_map[i][j] = 0
            else:
                all_flashing = False

    if all_flashing:
        break

print("Flashes synchronize at step:", step)

#!/bin/env python
import numpy as np

PART_1_STEPS = 2
PART_2_STEPS = 50

def apply_step(image, enhancement_algo):
    side = len(image) + 2
    if enhancement_algo[0] and not enhancement_algo[511]:
        matrix = np.full((side, side), image[0][0])
    else:
        matrix = np.full((side, side), False)
    matrix[1:-1,1:-1] = image

    next_matrix = np.full(matrix.shape, matrix)

    for i in range(1, next_matrix.shape[0] - 1):
        for j in range(1, next_matrix.shape[1] - 1):
            abc = ''.join([ "1" if elem else "0" for elem in matrix[i-1:i+2,j-1:j+2].flatten()])
            integer = int(abc, 2)
            next_matrix[i][j] = int(enhancement_algo[integer])

    next_matrix[0,] = next_matrix[1, 1]
    next_matrix[-1,] = next_matrix[1, 1]
    next_matrix[:,0] = next_matrix[1, 1]
    next_matrix[:,-1] = next_matrix[1, 1]
    return next_matrix


with open("input.txt") as f:
    lines = f.readlines()

enhancement_algo = [ int(i) for i in lines[0].strip().replace(".", "0").replace("#", "1")]

input_image = []
for line in lines[2:]:
    row = []
    for elem in line.strip():
        row.append(True if elem == "#" else False)
    input_image.append(row)


# Performances could be improved by pre-allocating the matrix
# since, given the number of steps, we know how big would it be
# 2 + n_steps + len(image)
side = len(input_image) + 4
enlarged_image = np.full((side, side), False)
enlarged_image[2:-2,2:-2] = input_image
image = enlarged_image
for i in range(PART_2_STEPS):
    image = apply_step(image, enhancement_algo)
print("Total lit pixels:", np.count_nonzero(image))
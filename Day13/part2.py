#!/bin/env python3

def fold(paper, axis, index):
    if axis == 'x':
        for row in paper:
            for i in range(len(row) - index):
                row[index - i] = row[index - i] or row[index + i]

    else:
        for i in range(len(paper) - index):
            row = paper[index + i]
            for j, dot in enumerate(row):
                paper[index - i][j] = paper[index-i][j] or dot


def cut(paper, axis, index):
    new_paper = []
    if axis == 'x':
        for row in paper:
            new_paper.append(row[:index])
    else:
        return paper[:index]

    return new_paper



with open("input.txt") as f:
    lines = f.readlines()

MAX_WIDTH = 1500
MAX_HEIGHT = 1500

paper = [ ]
for i in range(MAX_HEIGHT):
    paper.append([False] * MAX_WIDTH)

for line in lines:
    line = line.strip()
    if line == '': continue
    if "=" not in line:
        x, y = line.split(',')
        paper[int(y)][int(x)] = True

    else:
        raw_axis, index = line.split("=")
        axis = raw_axis[-1]
        index = int(index)
        fold(paper, axis, index)
        paper = cut(paper, axis, index)

for row in paper:
    for d in row:
        print('#' if d else " ", end="")
    print()

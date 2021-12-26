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



with open("input.txt") as f:
    lines = f.readlines()

MAX_WIDTH = 1500
MAX_HEIGHT = 1500

paper = [ ]
dots = 0
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
        if axis == 'x':
            for row in paper:
                for i in range(index):
                    dots += row[i]
        else:
            for i in range(index):
                for dot in paper[i]:
                    dots += dot
        break

print("Total dots:", dots)
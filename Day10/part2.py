#!/bin/env python3

ROUND_POINTS = 3
SQUARE_POINTS = 57
CURLY_POINTS = 1197
ANGLE_POINTS = 25137

ROUND = 0
SQUARE = 1
CURLY = 2
ANGLE = 3

with open("input.txt") as f:
    lines = f.readlines()

scores = []
for line in lines:
    stack = []
    corrupted = False
    for bracket in line.strip():
        if bracket == "(":stack.append(ROUND)
        if bracket == "[": stack.append(SQUARE)
        if bracket == "{": stack.append(CURLY)
        if bracket == "<": stack.append(ANGLE)
        

        if bracket == ")" and stack.pop() != ROUND: 
            corrupted = True
            break
        elif bracket == "]" and stack.pop() != SQUARE:
            corrupted = True
            break
        elif bracket == "}" and stack.pop() != CURLY:
            corrupted = True
            break
        elif bracket == ">" and stack.pop() != ANGLE:
            corrupted = True
            break

    if not corrupted:
        # the stack will contain the missing bracket in reverse order
        score = 0
        for bracket in stack[::-1]:
            score *= 5
            score += bracket + 1 # since brackets are stored as the points they give minus 1
        scores.append(score)


middle_score = sorted(scores)[len(scores)//2]
print("Middle score:", middle_score)

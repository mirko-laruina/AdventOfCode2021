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

syntax_error_score = 0
for line in lines:
    stack = []
    for bracket in line.strip():
        if bracket == "(": stack.append(ROUND)
        if bracket == "[": stack.append(SQUARE)
        if bracket == "{": stack.append(CURLY)
        if bracket == "<": stack.append(ANGLE)
        

        if bracket == ")" and stack.pop() != ROUND: 
            syntax_error_score += ROUND_POINTS
            break
        elif bracket == "]" and stack.pop() != SQUARE:
            syntax_error_score += SQUARE_POINTS
            break
        elif bracket == "}" and stack.pop() != CURLY:
            syntax_error_score += CURLY_POINTS
            break
        elif bracket == ">" and stack.pop() != ANGLE:
            syntax_error_score += ANGLE_POINTS
            break

print("Syntax error score:", syntax_error_score)
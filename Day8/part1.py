#!/bin/env python3

class Display:
    observations = []
    outputs = []

    def __init__(self, observations, outputs):
        self.observations = observations
        self.outputs = outputs

def get_pattern(patternString):
    return ''.join(sorted(patternString))
    pattern = 0
    for char in patternString:
        pattern = pattern | (1 << (ord(char) - ord('a')))
    return pattern

with open("input.txt") as f:
    lines = f.readlines()


displays = []
for line in lines:
    observed_patterns, outputs = line.strip().split("|")
    observed_patterns = [ get_pattern(i) for i in observed_patterns.strip().split() ]
    outputs = [ get_pattern(i) for i in outputs.strip().split() ]
    display = Display(observed_patterns, outputs)
    displays.append(display)


count = 0
for display in displays:
    for output in display.outputs:
        segments = len(output)
        if segments == 2 or segments == 4 or segments == 3 or segments == 7:
            count += 1

print("Count of 1, 4, 7 and 8s:", count)
#!/bin/env python3

from typing import Counter


with open("input.txt") as f:
    lines = f.readlines()

template = lines[0].strip()
produced_outputs = {}

for line in lines[2:]:
    pair, output = line.strip().split("->")
    pair = pair.strip()
    output = output.strip()

    produced_outputs[pair] = output


polymer = template
for step in range(10):
    next_polymer = []
    previous_char = polymer[0]
    next_polymer.append(previous_char)
    for char in polymer[1:]:
        generated = produced_outputs[previous_char + char]
        # print(f"{previous_char} + {char} = {generated}")
        next_polymer.append(generated)
        next_polymer.append(char)
        previous_char = char

    polymer = next_polymer
    # print(f"Length after step {step+1}: {len(next_polymer)}")


poly_dict = {}
for element in polymer:
    if element not in poly_dict:
        poly_dict[element] = 1
    else:
        poly_dict[element] += 1

poly_counts = sorted(poly_dict.values())
print(poly_dict)
difference = poly_counts[-1] - poly_counts[0]
print(f"Most common - least common difference:", difference)

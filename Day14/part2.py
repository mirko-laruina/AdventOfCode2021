#!/bin/env python3

def sum_counters(counters1, counters2):
    sum_counters = {}
    for key in counters1:
        sum_counters[key] = counters1[key]
    
    for key in counters2:
        if key in counters1:
            sum_counters[key] += counters2[key]
        else:
            sum_counters[key] = counters2[key]

    return sum_counters

def get_counters(polymer):
    poly_dict = {}
    for element in polymer:
        if element not in poly_dict:
            poly_dict[element] = 1
        else:
            poly_dict[element] += 1

    return poly_dict


cache = {}
def get_child_count(remaining_steps, outputs, parents):
    if remaining_steps == 0:
        return {}

    if remaining_steps in cache:
        if parents in cache[remaining_steps]:
            return cache[remaining_steps][parents]

    child = outputs[parents]

    counters = { child: 1 }
    left_counters = get_child_count(remaining_steps - 1, outputs, parents[0] + child)
    counters = sum_counters(counters, left_counters)
    right_counters = get_child_count(remaining_steps - 1, outputs, child + parents[1])
    counters = sum_counters(counters, right_counters)

    if remaining_steps not in cache:
        cache[remaining_steps] = {}
    cache[remaining_steps][parents] = counters
    return counters


with open("input.txt") as f:
    lines = f.readlines()

template = lines[0].strip()
produced_outputs = {}

for line in lines[2:]:
    pair, output = line.strip().split("->")
    pair = pair.strip()
    output = output.strip()

    produced_outputs[pair] = output

counters = get_counters(template)

MAX_STEPS = 40
previous_parent = template[0]
for parent in template[1:]:
    c = get_child_count(MAX_STEPS, produced_outputs, previous_parent + parent)
    previous_parent = parent
    counters = sum_counters(counters, c)

# print(counters)


poly_counts = sorted(counters.values())
difference = poly_counts[-1] - poly_counts[0]
print(f"Most common - least common difference:", difference)

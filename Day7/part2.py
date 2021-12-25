#!/bin/env python3
import sys

def get_diff_to_num(items, num):
    diff_sum = 0
    for item in items:
        distance = abs(item-num)
        diff_sum += distance * (distance + 1) / 2 
    return diff_sum

with open("input.txt") as f:
    positions = [ int(i) for i in f.readline().strip().split(",")]


# Cost function: sum of | xi - x0 | * | xi - x0 + 1 | * 1/2
# where the minimum x0 is bounded in (2*sum(xi) - n)/2n and (2*sum(xi) + n)/2n
# which is mean -/+ 0.5

mean = sum(positions) / len(positions)
trials = [mean, mean-0.5, mean+0.5]

min_fuel = sys.maxsize
min_position = -1
for trial in trials:
    rounded_trial = round(trial)
    fuel_consumption = get_diff_to_num(positions, rounded_trial)
    if(fuel_consumption < min_fuel):
        min_position = rounded_trial
        min_fuel = fuel_consumption

print("Aligned to horizontal position:", min_position)
print("Fuel consumption:", min_fuel)
#!/bin/env python3
import math

def get_median(items):
    return sorted(items)[len(items)//2]

def get_diff_to_num(items, num):
    diff_sum = 0
    for item in items:
        diff_sum += abs(item - num)
    return diff_sum



with open("input.txt") as f:
    positions = [ int(i) for i in f.readline().strip().split(",")]


mean = get_median(positions)
rounded_mean = round(mean)
fuel_consumption = get_diff_to_num(positions, rounded_mean)

print("Aligned to horizontal position:", rounded_mean)
print("Fuel consumption:", fuel_consumption)
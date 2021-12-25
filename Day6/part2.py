#!/bin/env python3
import numpy as np

FISH_MAX_DAYS = 7
FISH_FIRST_CYCLE_EXTRA = 2
SIM_DAYS = 256

fish_by_new_born = np.full(SIM_DAYS, -1, dtype=np.int64)
def get_fish_by_regeneration_day(current_day):
    if fish_by_new_born[current_day] != -1:
        return fish_by_new_born[current_day]
    
    if current_day + FISH_MAX_DAYS >= SIM_DAYS:
        return 1

    if current_day + FISH_MAX_DAYS + FISH_FIRST_CYCLE_EXTRA >= SIM_DAYS:
        fish_by_new_born[current_day] = 1 + get_fish_by_regeneration_day(current_day + FISH_MAX_DAYS)
    else:
        fish_by_new_born[current_day] = 1 + get_fish_by_regeneration_day(current_day + FISH_MAX_DAYS) + get_fish_by_regeneration_day(current_day + FISH_MAX_DAYS + FISH_FIRST_CYCLE_EXTRA)

    return fish_by_new_born[current_day]


with open("input.txt") as f:
    line = f.readline()
    fish = [ int(i) for i in line.strip().split(",")]

fish_produced = 0
for a_fish in fish:
    fish_produced += 1 + get_fish_by_regeneration_day(a_fish)

print("Total:", fish_produced)
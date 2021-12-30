#!/bin/env python3

# This solution could be improved quite a lot

def get_max_x_reached(starting_velocity):
    return 0.5 * (starting_velocity * starting_velocity) + starting_velocity

with open("input.txt") as f:
    line = f.readline()


part1, part2 = line.strip().split(",")
x_min, x_max = part1.split("x=")[1].split('..')
y_min, y_max = part2.split("y=")[1].split("..")

x_min = int(x_min)
x_max = int(x_max)
y_min = int(y_min)
y_max = int(y_max)

raised_y_max = y_max - y_min
raised_x_max = x_max - x_min

def is_target_hit(x0, y0):
    x = -x_min
    y = -y_min

    if(x0 > 0 and x_max < 0) or (x0 < 0 and x_max > 0):
        return False
    
    y_speed = y0
    x_speed = x0
    while y > y_min or y_speed > 0:

        x += x_speed
        y += y_speed

        if x_speed > 0: x_speed = x_speed - 1
        if x_speed < 0: x_speed = x_speed + 1
        y_speed = y_speed - 1

        if y >= 0 and y <= raised_y_max and x >= 0 and x <= raised_x_max:
            # print("---------")
            return True

    return False

count = 0
for xv in range(x_max+1):
    yv = 0
    while yv*yv <= (y_min - 1)*y_min :
        #print("Xv =", xv,", Yv =", yv)
        if(is_target_hit(xv, yv)): 
            count += 1
        
        if yv != 0:
            if(is_target_hit(xv, -yv)): 
                count += 1
        yv += 1

print("Count of valid (x, y) pairs:", count)

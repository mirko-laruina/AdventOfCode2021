#!/bin/env python3
import json, math

RIGHT = 1
LEFT = 0

def snailfish_apply_add(result):
    is_simplified = False
    while not is_simplified:
        exploded = explode(result)
        splitted = False
        if not exploded:
            #print("BEFORE split:", result)
            splitted = split(result, 0) or split(result, 1)
            #print("SPLIT:", result)

        if not exploded and not splitted:
            is_simplified = True

def is_numeric(number):
    return type(number) is int

def add(number, dir, value):
    while not is_numeric(number[dir]):
        number = number[dir]
    number[dir] += value

def handle_explosion(number, dir):
    if is_numeric(number[not dir]):
        # print(dir, number)
        number[not dir] += number[dir][not dir]
    else:
        add(number[not dir], dir, number[dir][not dir])
    to_add = number[dir][dir]
    number[dir] = 0
    return dir, to_add

def explode_child(number, depth):
    if is_numeric(number):
        return False, 0, 0

    if depth > 2:
        if not is_numeric(number[LEFT]):
            dir, to_add = handle_explosion(number, LEFT)
            return True, dir, to_add
        elif not is_numeric(number[RIGHT]):
            dir, to_add = handle_explosion(number, RIGHT)
            return True, dir, to_add
        else:
            return False, 0, 0
    else:
        success, dir, increase_qty = explode_child(number[0], depth+1)
        from_dir = LEFT
        if not success:
            success, dir, increase_qty = explode_child(number[1], depth+1)
            from_dir = RIGHT

        if success:
            if increase_qty == 0:
                return True, 0, 0
            if dir == from_dir:
                return success, dir, increase_qty

            if is_numeric(number[dir]):
                number[dir] += increase_qty
            else:
                add(number[dir], not dir, increase_qty)
            
            return True, dir, 0
        return False, 0, 0
        

def explode(number):
    #print("Exploding:", number)
    exploded, _, _ = explode_child(number, 0)

    if exploded:
        #print("Exploded into:", number)
        return True
    #print("Not exploded")
    return False

def split(number, where):
    if type(number[where]) is int:
        if number[where] >= 10:
            number[where] = [number[where]//2, math.ceil(number[where]/2)]
            return True
        return False

    return split(number[where], 0) or split(number[where], 1)


def get_magnitude(number):
    if is_numeric(number):
        return number
    
    return 3*get_magnitude(number[0]) + 2*get_magnitude(number[1])

with open("input.txt") as f:
    lines = f.readlines()

addenda = []
for line in lines:
    addendum = json.loads(line.strip())
    addenda.append(addendum)

print(addenda)

result = addenda[0]
print("  ", result)
for addendum in addenda[1:]:
    print("+ ", addendum)
    result = [result, addendum]
    snailfish_apply_add(result)
    print("= ", result)

magnitude = get_magnitude(result)
print("Magnitude:", magnitude)
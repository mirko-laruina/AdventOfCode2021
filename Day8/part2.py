#!/bin/env python3

def segment_diff(obs1, obs2):
    return [x for x in obs1 if x not in obs2]

def segment_common(obs1, obs2):
    return [x for x in obs1 if x in obs2]

def get_pattern(patternString):
    return ''.join(sorted(patternString))

def rewire_digit(digit, wirings):
    rewired_digit = []
    for char in digit:
        rewired_digit.append(chr(ord('a') + wirings.index(char)))

    return ''.join(sorted(rewired_digit))

class Display:
    observations = []
    outputs = []

    def __init__(self, observations, outputs):
        self.observations = observations
        self.outputs = outputs

    def decode(self):
        digits = [None] * 10
        wirings = [None] * 7
        for observation in self.observations:
            length = len(observation)
            if length == 3:
                digits[7] = observation
                #print("Digit 7:", digits[7])
            if length == 2:
                digits[1] = observation
                #print("Digit 1:", digits[1])
            if length == 4:
                digits[4] = observation
                #print("Digit 4:", digits[4])
            if length == 7:
                digits[8] = observation
                #print("Digit 8:", digits[8])

        # a
        wirings[0] = segment_diff(digits[7], digits[4])[0]
        #print(f"{wirings[0]} -> a")


        # digit 6 will be the one with 6 segments without one of the segments in digit 1
        for observation in self.observations:
            if len(observation) != 6: continue
            common_segments = segment_common(observation, digits[1])
            if len(common_segments) == 2: continue
            digits[6] = observation
            #print("Digit 6", digits[6])
            # f
            wirings[5] = common_segments[0]
            #print(f"{wirings[5]} -> f")
            # c
            wirings[2] = segment_diff(digits[1], [wirings[5]])[0]
            #print(f"{wirings[2]} -> c")
            break


        bd_segments = segment_diff(digits[4], digits[1])
        for observation in self.observations:
            common_segments = segment_common(observation, bd_segments)
            if len(common_segments) != 1: continue
            #print(observation)
            # it could be a 0, a 2 or a 3
            if len(observation) == 6:
                # it is a 0
                digits[0] = observation
                #print("Digit 0:", digits[0])
                # b
                wirings[1] = common_segments[0]
                #print(f"{wirings[1]} -> b")
                # d
                wirings[3] = segment_diff(digits[8], digits[0])[0]
                #print(f"{wirings[3]} -> d")
                continue
            
            if len(segment_common(observation, digits[4])) == 3:
                # it is a 3
                digits[3] = observation
                #print("Digit 3:", digits[3])
            else:
                digits[2] = observation
                #print("Digit 2:", digits[2])


        wirings[6] = segment_diff(digits[3], digits[4])
        wirings[6] = segment_diff(wirings[6], digits[1])
        wirings[6] = segment_diff(wirings[6], wirings[0])[0]
        digits[9] = ''.join(sorted([wirings[0], wirings[1], wirings[2], wirings[3], wirings[5], wirings[6]]))
        # e
        wirings[4] = segment_diff(digits[8], digits[9])[0]           

        digits[5] = ''.join(sorted([wirings[0], wirings[1], wirings[3], wirings[5], wirings[6] ]))

        #print(digits)
        #print(wirings)
        return digits, wirings




with open("input.txt") as f:
    lines = f.readlines()


displays = []
for line in lines:
    observed_patterns, outputs = line.strip().split("|")
    observed_patterns = [ get_pattern(i) for i in observed_patterns.strip().split() ]
    outputs = [ get_pattern(i) for i in outputs.strip().split() ]
    display = Display(observed_patterns, outputs)
    displays.append(display)


sum = 0
for display in displays:
    digits, wirings = display.decode()
    display_counter = 0
    #for i, digit in enumerate(digits):
    #    print(digit)
    #    print(i, rewire_digit(digit, wirings))
    for output in display.outputs:
        display_counter += digits.index(output)
        display_counter *= 10

    sum += display_counter // 10


print("Sum of decoded outputs:", sum)
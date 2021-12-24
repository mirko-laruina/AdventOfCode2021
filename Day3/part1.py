#!/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

bitSequenceLen = len(lines[0].strip())
bitCounter = []
for i in range(bitSequenceLen):
    bitCounter.append(0)

for line in lines:
    for i, char in enumerate(line.strip()):
        bitCounter[i] += int(char)

gamma_rate = 0
eps_rate = 0
for i in range(len(bitCounter)):
    bitValue = bitCounter[i] > len(lines) / 2
    print(bitCounter[i], bitValue)
    shift = len(bitCounter) - i - 1
    gamma_rate = gamma_rate | ( bitValue << shift )
    eps_rate = eps_rate | ((0 if bitValue else 1) << shift )

print("Gamma rate:", gamma_rate)
print("Epsilon rate:", eps_rate)
print("Product:", gamma_rate * eps_rate)


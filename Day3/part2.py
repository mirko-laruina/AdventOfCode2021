#!/bin/env python3


def countBits(lines):
    bitCounters = []

    for i in range(len(lines[0].strip())):
        bitCounters.append(0)

    for line in lines:
        for i, char in enumerate(line.strip()):
            bitCounters[i] += int(char)

    return bitCounters

def oxygenCriteria(ones, total):
    return ones >= total / 2

def co2Criteria(ones, total):
    return ones < total / 2


def getLineByCriteria(lines, criteria):
    validLines = lines
    currentBit = 0
    while len(validLines) > 1 :
        nextValidLines = []
        counters = countBits(validLines)
        criteriaGood = criteria(counters[currentBit], len(validLines))        
        for line in validLines:
            if(int(line[currentBit]) == criteriaGood):
                nextValidLines.append(line)
        currentBit += 1
        validLines = nextValidLines
    return int(validLines[0], 2)


with open("input.txt") as f:
    lines = f.readlines()

oxygen = getLineByCriteria(lines, oxygenCriteria)
co2 = getLineByCriteria(lines, co2Criteria)
print("Oxygen:", oxygen)
print("CO2:", co2)
print("Product:", oxygen * co2)



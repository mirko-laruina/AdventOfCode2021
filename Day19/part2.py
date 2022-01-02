import itertools

class Scanner:
    def __init__(self, id) -> None:
        self.beacons = []
        self.id = id
        self.offset = None
        self.signs= (1, 1, 1)
        self.axis = (0, 1, 2)

    def add_beacon(self, beacon):
        self.beacons.append(beacon)

    def __repr__(self) -> str:
        return f"Scanner{self.id}"

class Beacon:
    def __init__(self, position) -> None:
        self.position = position

    def distance(self, other_beacon) -> int:
        return manhattan_distance(self.position, other_beacon.position)

    def __repr__(self) -> str:
        return f"Beacon {self.position}"
    
    def __lt__(self, other):
        return self.position < other.position

def manhattan_distance(position_1, position_2):
    result = 0
    for p1, p2 in zip(position_1, position_2):
        result += abs(p2 - p1)
    return result

def get_permutations():
    n = 0
    while n < 48:
        negs = n % 8
        signs = (1 if negs & 0x4 else -1, 1 if negs & 0x2 else -1, 1 if negs & 0x1 else -1)
        rot = n >> 3
        if rot == 0:
            axis = (0, 1, 2)
        elif rot == 1:
            axis = (0, 2, 1)
        elif rot == 2:
            axis = (1, 0, 2)
        elif rot == 3:
            axis = (1, 2, 0)
        elif rot == 4:
            axis = (2, 0, 1)
        else:
            axis = (2, 1, 0)
        n += 1
        yield axis, signs


def apply_permutation(beacons, axis, sign):
    adj_beacons = []
    for beacon in beacons:
        adj_position = beacon.position.copy()
        adj_position = [ a*b for a, b in zip(adj_position, sign)]
        adj_position = [ adj_position[axis[i]] for i in range(len(adj_position))]

        adj_beacon = Beacon(adj_position)
        adj_beacons.append(adj_beacon)
    return adj_beacons

def reverse_axis(axis):
    reversed_axis = []
    for i in range(3):
        reversed_axis.append(axis.index(i))
    return reversed_axis


with open("input.txt") as f:
    lines = f.readlines()

scanners = []
scanner_id = -1
for line in lines:
    line = line.strip()
    if line == '': continue
    if 'scanner' in line:
        scanner_id += 1
        current_scanner = Scanner(scanner_id)
        scanners.append(current_scanner)
    else:
        beacon = Beacon([int(i) for i in line.split(',')])
        current_scanner.add_beacon(beacon)

def get_distance_counters(beacons_1, beacons_2):
    distances = {}
    for beacon_1 in beacons_1:
        for beacon_2 in beacons_2:
            distance = beacon_2.distance(beacon_1)
            beacon_couple = (beacon_2, beacon_1)
            if distance not in distances:
                distances[distance] = [1, [ beacon_couple ]]
            else:
                distances[distance][0] += 1
                distances[distance][1].append(beacon_couple)
    return distances

def get_majority_diff(beacon_pairs):
    counter = {}
    good_diff = None
    for pair in beacon_pairs:
        diff = tuple([(a - b) for a, b in zip(pair[0].position, pair[1].position)])
        if diff not in counter:
            counter[diff] = 1
        else:
            counter[diff] += 1
        if counter[diff] > 11:
            good_diff = diff
            break
    return good_diff


def try_all_permutations(scanner_base, scanner_adj):
    for axis, signs in get_permutations():
        adj_beacons = apply_permutation(scanner_adj.beacons, axis, signs)
        distances = get_distance_counters(adj_beacons, scanner_base.beacons)

        for distance in distances:
            count = distances[distance][0]
            if count > 11 and distance != 0:

                beacon_pairs = distances[distance][1]
                print("-------------")
                print(f"BASE: scanner {scanner_base.id} with OFFSET {scanner_base.offset}, signs {scanner_base.signs} and axis {scanner_base.axis}")
                print(f"ADJUSTED: scanner {scanner_adj.id} with sign {signs} and axis {signs}")

                # A beacon could be misclasified as common if it provides the same manathann distance
                # We can check if it is valid with the 3d distances
                good_diff = get_majority_diff(beacon_pairs)
                if good_diff is None:
                    print("************** FAKE ***************")
                    continue

                print(f"FOUND OFFSET: {good_diff}")
                scanner_adj.offset = good_diff
                scanner_adj.signs = signs
                scanner_adj.axis = axis

                for beacon in adj_beacons:
                    beacon.position = [b + o for b, o in zip(beacon.position, scanner_adj.offset)]

                scanner_adj.beacons = adj_beacons
                print("-------------")
                return True

at_least_one = True
scanners[0].offset = (0, 0, 0)
open_scanners = [ scanners[0] ]
unknown_scanners = scanners.copy()
unknown_scanners.remove(scanners[0])
while at_least_one:
    at_least_one = False
    for scanner_base in open_scanners.copy():
        for scanner_adj in unknown_scanners.copy():
            success = try_all_permutations(scanner_base, scanner_adj)
            if success:
                open_scanners.append(scanner_adj)
                unknown_scanners.remove(scanner_adj)
                at_least_one = True
        open_scanners.remove(scanner_base)

for scanner in scanners:
    print(f"Scanner {scanner.id} with offset {scanner.offset}")

max_distance = -1
for scanner_1, scanner_2 in itertools.combinations(scanners, 2):
    distance = manhattan_distance(scanner_1.offset, scanner_2.offset)
    if distance > max_distance:
        max_distance = distance

print("Max distance:", max_distance)
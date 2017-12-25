import numpy as np


def update_state(states, deltas, ranges, length):
    states += deltas
    for i in range(length):
        if states[i] in {0, ranges[i] - 1}:
            deltas[i] = -deltas[i]
    return states, deltas


def get_firewall_score(data, offset):
    length = max(data.keys())
    deltas = np.zeros((length+1,))
    ranges = np.zeros((length+1,))
    states = np.zeros((length+1,))
    for key in data.keys():
        ranges[key] = data[key]
        if ranges[key] > 1:
            deltas[key] = 1
    for _ in range(offset):
        states, deltas = update_state(states, deltas, ranges, length)
    for block in range(length):
        if states[block] == 0 and ranges[block] > 0:
            return False
        states, deltas = update_state(states, deltas, ranges, length)
    return True


if __name__ == "__main__":
    with open("input.txt") as filename:
        lines = [line for line in filename.read().split("\n") if line]
    data = {}
    for line in lines:
        line = line.split(":")
        data[int(line[0])] = int(line[1])
    success = False
    offset = 0
    while not success:
        success = get_firewall_score(data, offset)
        offset += 1
        print(offset)
    print(offset - 1)

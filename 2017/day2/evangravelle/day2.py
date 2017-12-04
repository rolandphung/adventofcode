import numpy as np


def checksum1(data):
    mins = np.min(data, axis=1)
    maxs = np.max(data, axis=1)
    checksum = np.sum(maxs - mins, axis=0)
    return checksum


# I should break early, by making the inner 2 loops a separate function and returning if checksum is added to
def checksum2(data):
    sorted_data = np.flip(np.sort(data, axis=1), axis=1)
    checksum = 0
    for row in range(sorted_data.shape[0]):
        for ind1 in range(sorted_data.shape[1]):
            for ind2 in range(ind1 + 1, len(sorted_data[row, :])):
                if sorted_data[row, ind1] % sorted_data[row, ind2] == 0:
                    checksum += sorted_data[row, ind1] / sorted_data[row, ind2]

    return checksum


if __name__ == "__main__":
    data = np.loadtxt('input.txt')
    sum1 = checksum1(data)
    sum2 = checksum2(data)
    print sum1, sum2


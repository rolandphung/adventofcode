import numpy as np


def spiral_dist(data):
    dist1 = np.ceil(np.sqrt(data))
    dist1 = dist1 / 2 if dist1 % 2 == 0 else (dist1 - 1) / 2
    closest1 = (2*dist1 + 1)**2 - dist1
    closest2 = closest1 - 2*dist1
    closest3 = closest2 - 2*dist1
    closest4 = closest3 - 2*dist1
    closests = np.array([closest1, closest2, closest3, closest4])
    dist2 = np.min(np.abs(data - closests))
    return dist1 + dist2


def first_larger_val(data):
    vec = np.array([1, 0]).T
    rot = np.array([[0, -1], [1, 0]])
    steps = 1
    ctr = 0
    key = np.array([0, 0])
    vals = {tuple(key): 1}
    while True:
        if ctr < np.floor(steps):
            key += vec
            right = vals.get(tuple(key + np.array([1, 0])), 0)
            ru = vals.get(tuple(key + np.array([1, 1])), 0)
            up = vals.get(tuple(key + np.array([0, 1])), 0)
            lu = vals.get(tuple(key + np.array([-1, 1])), 0)
            left = vals.get(tuple(key + np.array([-1, 0])), 0)
            ld = vals.get(tuple(key + np.array([-1, -1])), 0)
            down = vals.get(tuple(key + np.array([0, -1])), 0)
            rd = vals.get(tuple(key + np.array([1, -1])), 0)
            vals[tuple(key)] = right + ru + up + lu + left + ld + down + rd
            ctr += 1
            if vals[tuple(key)] > data:
                return vals[tuple(key)]
        else:
            ctr = 0
            steps += 0.5
            vec = np.dot(rot, vec)


if __name__ == "__main__":
    data = 289326
    dist = spiral_dist(data)
    print dist

    val = first_larger_val(data)
    print val


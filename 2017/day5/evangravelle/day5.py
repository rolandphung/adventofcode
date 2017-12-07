import numpy as np


def get_steps(vec):
    steps = 0
    ind = 0
    vec_len = len(vec)
    while True:
        prev_ind = ind
        ind += vec[prev_ind]
        steps += 1
        if ind < 0 or ind >= vec_len:
            return steps
        if vec[prev_ind] >= 3:
            vec[prev_ind] -= 1
        else:
            vec[prev_ind] += 1


if __name__ == "__main__":
    with open("input.txt") as filename:
        lines = [line for line in filename.read().split() if line]
    vec = np.zeros((len(lines)), dtype=np.int32)
    for ind, line in enumerate(lines):
        vec[ind] = int(line)
    num_steps = get_steps(vec)
    print(num_steps)

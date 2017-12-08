import numpy as np


def steps_before_dup(loads):
    steps = 0
    key = tuple(loads)
    balance_ind = np.argmax(loads)
    loads_len = loads.size
    saved_keys = {}
    while key not in saved_keys:
        saved_keys[key] = steps
        # rebalance
        num_loads_to_balance = loads[balance_ind % loads_len]
        loads[balance_ind % loads_len] = 0
        for ctr in range(1, num_loads_to_balance + 1):
            loads[(balance_ind + ctr) % loads_len] += 1

        key = tuple(loads)
        steps += 1
        balance_ind = np.argmax(loads)

    return steps - saved_keys[key]


if __name__ == "__main__":
    loads = np.array([10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6])
    num_steps = steps_before_dup(loads)
    print(num_steps)

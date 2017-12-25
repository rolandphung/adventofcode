import numpy as np


def load_data():
    with open("input.txt") as filename:
        lines = filename.read().split("\n")
    lines = [line.split(" ") for line in lines if line]
    L_size = int(lines[-1][0])
    L = np.zeros((L_size + 1, L_size + 1))
    for line in lines:
        ind1 = int(line[0])
        for entry in line[2:]:
            ind2 = int(entry.strip(","))
            L[ind1, ind2] = 1
            L[ind2, ind1] = 1
    return L


def get_nodes_subgraph(L, node):
    queue = [node]
    num = 0
    used = []
    while queue:
        ind = queue.pop()
        used.append(ind)
        num += 1
        possibles = np.nonzero(L[ind, :])
        for possible in possibles[0]:
            if possible not in used:
                queue.append(possible)
    return used


def get_num_groups(L):
    num_loops = L.shape[0]
    to_dos = [True for _ in range(num_loops)]
    num_groups = 0
    for i in range(num_loops):
        if to_dos[i]:
            num_groups += 1
            used = get_nodes_subgraph(L, i)
            for node in used:
                L[node, :] = 0
                L[:, node] = 0
                to_dos[node] = False
    return num_groups


if __name__ == "__main__":
    mat = load_data()
    test = np.array([[1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])
    num_groups = get_num_groups(mat)
    print(num_groups)

import random


def make_tree(lines):
    tree = {}
    for line in lines:
        data = line.split(" ")
        if len(data) >= 4:
            data = [x.strip(",") for x in data]
            data[1] = int(data[1].strip("()"))
            for key in data[3:]:
                tree[key] = data[0]
    return tree


def make_tree2(lines):
    tree = {}
    for line in lines:
        data = line.split(" ")
        if len(data) == 2:
            tree[data[0]] = data[1]
        else:
            for child in data[3:]:
                tree[child] = data[0]
    return tree


def get_root(tree):
    key = random.choice(list(tree.keys()))
    while key in tree.keys():
        key = tree[key]
    return key


if __name__ == "__main__":
    with open("input.txt") as filename:
        lines = [line for line in filename.read().split("\n") if line]
    tree = make_tree(lines)
    root = get_root(tree)
    print(root)

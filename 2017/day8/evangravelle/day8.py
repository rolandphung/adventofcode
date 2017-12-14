"""Example input
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""


def update_val(str, vals, key, delta):
    if str == "inc":
        vals[key] += delta
        tmp_max = vals[key]
    else:
        vals[key] -= delta
        tmp_max = float("NaN")
    return vals, tmp_max


if __name__ == "__main__":
    with open("input.txt") as filename:
        lines = [line for line in filename.read().split("\n") if line]
    vals = {}
    max_val = 0
    for line in lines:
        line = line.split(" ")
        key_to_mod = line[0]
        key_to_check = line[4]
        op = line[5]
        thresh = int(line[6])
        to_update = False
        if key_to_mod not in vals.keys():
            vals[key_to_mod] = 0
        if key_to_check not in vals.keys():
            vals[key_to_check] = 0
        if op == ">" and vals[key_to_check] > thresh:
            to_update = True
        elif op == "<" and vals[key_to_check] < thresh:
            to_update = True
        elif op == "==" and vals[key_to_check] == thresh:
            to_update = True
        elif op == "!=" and vals[key_to_check] != thresh:
            to_update = True
        elif op == "<=" and vals[key_to_check] <= thresh:
            to_update = True
        elif op == ">=" and vals[key_to_check] >= thresh:
            to_update = True

        if to_update:
            vals, tmp_max = update_val(line[1], vals, key_to_mod, int(line[2]))
            max_val = max(max_val, tmp_max)

    mx = max(vals.values())
    print(mx)
    print(max_val)

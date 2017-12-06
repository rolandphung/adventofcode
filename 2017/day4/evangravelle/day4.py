def num_valid(lines):
    num = len(lines)
    for line in lines:
        dups = {}
        for entry in line.split(" "):
            if entry in dups:
                num -= 1
                break
            else:
                dups[entry] = True
    return num


def num_valid_harder(lines):
    num = len(lines)
    for line in lines:
        dups = {}
        for entry in line.split(" "):
            sorted_entry = ''.join(sorted(entry))
            if sorted_entry in dups:
                num -= 1
                break
            else:
                dups[sorted_entry] = True
    return num


if __name__ == "__main__":
    with open("input.txt", "r") as filename:
        lines = [line for line in filename.read().split("\n") if line]
    num1 = num_valid(lines)
    num2 = num_valid_harder(lines)
    print num1, num2


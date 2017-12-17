"""Knot Hash"""


def hash_list(lengths):
    list_size = 256
    nums = list(range(list_size))
    pos = 0
    skip_size = 0
    for length in lengths:
        if pos + length >= list_size:
            new_ind = (pos + length) % list_size
            tmp = nums[pos:list_size]
            tmp.extend(nums[0:new_ind])
            tmp.reverse()
            nums[pos:list_size] = tmp[0:list_size - pos]
            nums[0:new_ind] = tmp[list_size - pos:length]
        else:
            nums[pos:pos+length] = nums[pos:pos+length][::-1]
        pos = (pos + length + skip_size) % list_size
        skip_size += 1
    return nums


if __name__ == "__main__":
    with open("input.txt") as filename:
        lengths = filename.read().strip("\n").split(",")
        lengths = [int(length) for length in lengths]
    new_list = hash_list(lengths)
    print(new_list[0] * new_list[1])

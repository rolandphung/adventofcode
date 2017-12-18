"""Knot Hash"""


def hash_list(lengths):
    list_size = 256
    nums = list(range(list_size))
    pos = 0
    skip_size = 0
    for _ in range(64):
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


def dense_hash(sparse_hash):
    dense_hash = []
    for i in range(16):
        val = sparse_hash[16*i]
        for j in range(1, 16):
            val = val ^ sparse_hash[16*i + j]
        dense_hash.append(val)
    return dense_hash


if __name__ == "__main__":
    with open("input.txt") as filename:
        lengths = filename.read().strip("\n")
        lengths = [ord(length) for length in lengths]
    lengths.extend([17, 31, 73, 47, 23])
    new_list = hash_list(lengths)
    dense_list = dense_hash(new_list)
    hex_list = [hex(element)[2:4] for element in dense_list]
    knot_hash = "".join(hex_list)
    print(knot_hash)

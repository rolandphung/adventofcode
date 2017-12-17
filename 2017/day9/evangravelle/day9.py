"""Garbage Collector"""


def collect_garbage(stream):
    score, num_chars, i = 0, 0, 0
    stack = []
    while i < len(stream):

        if not stack:
            stack.append(stream[i])
        elif stack[-1] == "<":
            if stream[i] == "!":
                i += 1
            elif stream[i] == ">":
                stack.pop()
            else:
                num_chars += 1
        elif stack[-1] == "{":
            if stream[i] == "!":
                i += 1
            elif stream[i] == "}":
                score += len(stack)
                stack.pop()
            elif stream[i] == "{":
                stack.append(stream[i])
            elif stream[i] == "<":
                stack.append(stream[i])
        i += 1
    if stack:
        print(stack)
        print("The stack should be empty!")
    return score, num_chars


if __name__ == "__main__":
    with open("input.txt") as filename:
        stream = filename.read().strip("\n")

    score, num_chars = collect_garbage(stream)
    print([score, num_chars])

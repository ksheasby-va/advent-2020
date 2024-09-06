def get_number(string_in):
    low_index = -1
    low_number = -1
    high_number = -1
    for i, n in enumerate(string_in):
        if n.isdigit():
            if low_index == -1:
                low_index = i
                low_number = n
                high_number = n
            else:
                high_number = n
    return int(low_number + high_number)


def add_all_numbers(filename):
    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        total += get_number(line.strip())
    return total


if __name__ == '__main__':
    print(add_all_numbers("day_01_input.txt"))

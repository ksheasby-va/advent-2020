from day_02_part_01 import parse_game


def sum_of_powers(filename):
    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        _, max_blue, max_red, max_green = parse_game(line.strip())
        total += max_blue * max_red * max_green

    return total


if __name__ == '__main__':
    total = sum_of_powers("day_02_input.txt")
    print(total)

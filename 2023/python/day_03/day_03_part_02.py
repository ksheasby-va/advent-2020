from day_03_part_01 import read_file_into_grid, find_number


def is_adjacent_to_numbers(x, y, grid):
    adjacents = [-1, 0, 1]
    adjacent_number_locations = []
    for i in adjacents:
        if x + i < 0 or x + i >= len(grid):
            continue
        for j in adjacents:
            if y + j < 0 or y + j >= len(grid[0]):
                continue
            if i == 0 and j == 0:
                continue
            if grid[x + i][y + j] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                adjacent_number_locations.append((x + i, y + j))
    return adjacent_number_locations


def parse_grid(filename):
    grid = read_file_into_grid(filename)
    # print(grid)
    number_set = set()
    for i, n in enumerate(grid):
        for j, m in enumerate(n):
            if m == '*':
                adjacents = is_adjacent_to_numbers(i, j, grid)
                if len(adjacents) < 2:
                    continue
                numbers = []
                for adjacent in adjacents:
                    numbers.append(find_number(adjacent[0], adjacent[1], grid)[0])
                    print(f"found {find_number(adjacent[0], adjacent[1], grid)} at {adjacent[0]}, {adjacent[1]}")
                numbers = list(set(numbers))
                print(f"numbers: {numbers}")
                if len(numbers) == 2:
                    number_set.add(numbers[0] * numbers[1])
    print(number_set)
    total = 0
    for x in number_set:
        total += x
    return total


if __name__ == '__main__':
    print(parse_grid("day_03_input.txt"))

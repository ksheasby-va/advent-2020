def is_adjacent_to_symbol(x, y, grid):
    adjacents = [-1, 0, 1]
    for i in adjacents:
        if x + i < 0 or x + i >= len(grid):
            continue
        for j in adjacents:
            if y + j < 0 or y + j >= len(grid[0]):
                continue
            if i == 0 and j == 0:
                continue
            if grid[x + i][y + j] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return True
    return False


def read_file_into_grid(filename):
    with open(filename, 'r') as file:
        content = file.read()
    lines = content.splitlines()
    grid = [list(line) for line in lines]
    return grid


def find_number(x, y, grid):
    start = y
    end = y
    while end < len(grid[0]):
        last_value = grid[x][end]
        if not last_value.isdigit():
            break
        end += 1
    while start >= 0:
        first_value = grid[x][start]
        if not first_value.isdigit():
            start += 1
            break
        if start == 0:
            break
        start -= 1

    return int(''.join(grid[x][start:end])), start, end


def parse_grid(filename):
    grid = read_file_into_grid(filename)
    # print(grid)
    number_set = set()
    for i, n in enumerate(grid):
        for j, m in enumerate(n):
            if m.isdigit() and is_adjacent_to_symbol(i, j, grid):
                # print(f"found {m} at {i}, {j}")
                # print(i, find_number(i, j, grid))
                number_set.add((i, find_number(i, j, grid)))
    # print(number_set)
    total = 0
    for i, n in number_set:
        # print(i, n[0])
        total += n[0]
    return total


if __name__ == '__main__':
    print(parse_grid("day_03_input.txt"))

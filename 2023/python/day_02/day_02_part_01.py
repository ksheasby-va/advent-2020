import re


def max_of_list(lst):
    max_val = -1
    for i in lst:
        if int(i) > max_val:
            max_val = int(i)
    return max_val


def parse_game(game):
    blue_pattern = re.compile(r'(\d+) blue')
    red_pattern = re.compile(r'(\d+) red')
    green_pattern = re.compile(r'(\d+) green')
    game_number_pattern = re.compile(r'Game (\d+):')
    game_number = re.search(game_number_pattern, game).group(1)
    # print(game_number)

    max_blue = max_of_list(re.findall(blue_pattern, game))
    max_red = max_of_list(re.findall(red_pattern, game))
    max_green = max_of_list(re.findall(green_pattern, game))

    # print(max_blue, max_red, max_green)

    return int(game_number), max_blue, max_red, max_green


def possible_game(blue, red, green):
    if blue > 14:
        return False
    if red > 12:
        return False
    if green > 13:
        return False
    return True


def add_all_numbers(filename):
    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        parsed_game = parse_game(line.strip())
        if possible_game(*parsed_game[1:]):
            total += parsed_game[0]
    return total


if __name__ == '__main__':
    total = add_all_numbers("day_02_input.txt")
    print(total)

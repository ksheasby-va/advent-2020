import re


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


def find_overlapping_matches(string_in):
    pattern = re.compile(r'one|two|three|four|five|six|seven|eight|nine|\d')
    matches = []
    start = 0
    while start < len(string_in):
        match = re.search(pattern, string_in[start:])
        if not match:
            break
        matches.append(match.group())
        start += match.start() + 1
    return matches


def get_number_from_word(word):
    matches = find_overlapping_matches(word)
    # print(matches)
    first = matches[0]
    last = matches[-1]
    number_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    res = int(number_map.get(first, first) + number_map.get(last, last))
    # print(res)
    return res


def add_all_numbers(filename):
    total = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    for line in lines:
        total += get_number_from_word(line.strip())
    return total


if __name__ == '__main__':
    print(add_all_numbers("day_01_input.txt"))
    # print(get_number_from_word("xtwone3four"))

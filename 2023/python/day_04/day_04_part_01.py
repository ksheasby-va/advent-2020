def parse_cards(filename):
    with open(filename, 'r') as file:
        content = file.read()
    lines = content.splitlines()
    all_winners = []
    all_haves = []
    for line in lines:
        # print(line)
        pieces = line.split('|')
        # print(pieces)
        winners = set()
        have = set()
        for n in pieces[0].split(' '):
            if n.isdigit():
                winners.add(n)
        for n in pieces[1].split(' '):
            if n.isdigit():
                have.add(n)

        # print(winners)
        # print(have)
        all_winners.append(winners)
        all_haves.append(have)

    return all_winners, all_haves


def calculate_points(all_winners, all_haves):
    total = 0
    for i, h in enumerate(all_haves):
        row_total = 0
        # print(i, h)
        for j in h:
            if j in all_winners[i]:
                if row_total == 0:
                    row_total = 1
                else:
                    row_total *= 2
        total += row_total
    return total


if __name__ == '__main__':
    winners, haves = parse_cards("day_04_input.txt")
    print(calculate_points(winners, haves))

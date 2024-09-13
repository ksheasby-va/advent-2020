from os import times

from day_04_part_01 import parse_cards


def count_cards(all_winners, all_haves):
    total = {}
    number_of_each_card = {}
    for i, h in enumerate(all_haves):
        for l in range(number_of_each_card.get(i, 1)):
            row_total_winners = 0
            for j in h:
                if j in all_winners[i]:
                    row_total_winners += 1
            total[i + 1] = row_total_winners
            for k in range(row_total_winners):
                number_of_each_card[i + k + 1] = number_of_each_card.get(i + k + 1, 0) + 1
            else:
                number_of_each_card[i + 1] = number_of_each_card.get(i + 1, 0) + 1
    return total, number_of_each_card


if __name__ == '__main__':
    winners, haves = parse_cards("day_04_example_input.txt")
    print(count_cards(winners, haves))

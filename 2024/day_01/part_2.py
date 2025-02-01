from part_1 import split_input

def calculate_similarity(filename):
    lefts, rights = split_input(filename)

    lefts = sorted(lefts)
    rights = sorted(rights)
    # print(lefts, rights)

    total = 0
    for v in lefts:
        copies = 0
        for w in rights:
            if v == w:
                copies += 1
            elif w > v:
                break
        total += copies * v
    print(total)

    

if __name__ == '__main__':
    print('Hello, World!123')
    calculate_similarity('input.txt')
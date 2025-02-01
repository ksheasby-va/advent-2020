def calculate_difference(filename):
    lefts, rights = split_input(filename)

    lefts = sorted(lefts)
    rights = sorted(rights)
    # print(lefts, rights)

    total = 0
    for i, v in enumerate(lefts):
        total += abs(v - rights[i])

    print(total)

def split_input(filename):
    with open(filename, 'r') as f:
        lefts = []
        rights = []
        for r in f.readlines():
            left, right = r.split()
            lefts.append(int(left))
            rights.append(int(right))
    return lefts,rights
            

if __name__ == '__main__':
    print('Hello, World!123')
    calculate_difference('input.txt')
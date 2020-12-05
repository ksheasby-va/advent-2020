def run(filename):
    with open(filename, 'r') as f:
        passwords = []
        for l in f.readlines():
            split = l.split(' ')
            numbers = split[0].split('-')
            d = {
                "position_1": int(numbers[0]),
                "position_2": int(numbers[1]),
                "letter": split[1][0],
                "password": split[2],
            }
            passwords.append(d)

    total = 0
    for p in passwords:
        pos_1 = p.get('position_1')
        pos_2 = p.get('position_2')
        pw = p.get('password').strip()
        if pw[pos_1 - 1] == p.get('letter'):
            if pw[pos_2 - 1] == p.get('letter'):
                continue
            total += 1
            continue
        elif pw[pos_2 - 1] == p.get('letter'):
            if pw[pos_1 - 1] == p.get('letter'):
                continue
            total += 1
            continue

    return total

if __name__ == '__main__':
    print run('input.txt')

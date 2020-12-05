def run(filename):
    with open(filename, 'r') as f:
        passwords = []
        for l in f.readlines():
            split = l.split(' ')
            numbers = split[0].split('-')
            d = {
                "min": int(numbers[0]),
                "max": int(numbers[1]),
                "letter": split[1][0],
                "password": split[2],
            }
            passwords.append(d)

    total = 0
    for p in passwords:
        count = p.get('password').count(p.get('letter'))
        if p.get('min') <= count and count <= p.get('max'):
            total += 1

    return total

if __name__ == '__main__':
    print run('input.txt')

def run(file_name):
    totals = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for s in slopes:
        count = 0
        skipped = 0
        with open(file_name, 'r') as f:
            for num, r in enumerate(f.readlines()):
                if not num % s[1] == 0:
                    skipped += 1
                    continue
                index = ((num - skipped) * s[0])
                longer_row = r.strip() * 75
                if longer_row[index] == '#':
                    count += 1
            totals.append(count)


    return totals[0] * totals[1] * totals[2] * totals[3] * totals[4]

if __name__ == '__main__':
    print run('input.txt')

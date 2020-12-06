def run(file_name):
    passports = []
    with open(file_name, 'r') as f:
        pp = {}
        for r in f.readlines():
            if len(r) < 2:
                passports.append(pp)
                pp = {}
                continue
            pieces = r.split(' ')
            for p in pieces:
                pp[p.split(':')[0]] = p.split(':')[1]


    count = 0
    for q in passports:
        if len(q) == 8:
            count += 1
            continue
        if len(q) == 7:
            if q.get('cid') is None:
                count += 1

    return count


if __name__ == '__main__':
    print run('input.txt')

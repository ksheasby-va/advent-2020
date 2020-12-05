def run(file_name):
    with open(file_name, 'r') as f:
        large = []
        small = []
        for r in f.readlines():
            if int(r) > 1010:
                large.append(int(r))
            else:
                small.append(int(r))

    for i in large:
        for j in small:
            if i + j == 2020:
                return i * j

if __name__ == '__main__':
    print run('input.txt')

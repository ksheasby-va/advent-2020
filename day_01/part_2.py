def run(file_name):
    with open(file_name, 'r') as f:
        numbers_1 = []
        numbers_2 = []
        numbers_3 = []
        for r in f.readlines():
            numbers_1.append(int(r))
            numbers_2.append(int(r))
            numbers_3.append(int(r))

    for i in numbers_1:
        for j in numbers_2:
            for k in numbers_3:
                if i + j + k == 2020:
                    return i * j * k

if __name__ == '__main__':
    print run('input.txt')

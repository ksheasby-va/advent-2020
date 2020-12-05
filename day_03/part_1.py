def run(file_name):
    count = 0
    with open(file_name, 'r') as f:
        for num, r in enumerate(f.readlines()):
            index = (num * 3)
            longer_row = r.strip() * 33
            if longer_row[index] == '#':
                count += 1

    return count

if __name__ == '__main__':
    print run('input.txt')

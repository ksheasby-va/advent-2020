def count_safe_reports(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    count = 0
    for l in lines:
        valid = True
        increasing = False
        decreasing = False
        line = l.split()
        line = [int(x) for x in line]
        if sorted(line) != line and sorted(line, reverse=True) != line:
            # print('invalid not sorted:', line)
            valid = False
            continue
        for i, v in enumerate(line):
            v2 = line[i+1] if i+1 < len(line) else None
            if not v2:
                break
            if v == line[i+1]:          
                # print('invalid equals:', line)
                valid = False
                break
            if i == 0:
                if v < v2 and not decreasing:
                    increasing = True
                elif v > v2 and not increasing:
                    decreasing = True
            if increasing and v > v2:
                # print('invalid inceasing:', line)
                valid = False
                break
            if decreasing and v < v2:
                # print('invalid decreasing:', line)
                valid = False
                break
            if abs(v - v2) > 3:
                # print('invalid difference:', line)
                valid = False
                break
        if valid:
            count += 1

    return count

if __name__ == '__main__':
    print(count_safe_reports('example_input.txt'))
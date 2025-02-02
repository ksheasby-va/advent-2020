def count_safe_reports(file_path: str) -> int:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    count = 0
    for l in lines:
        valid = True
        line = l.split()
        line = [int(x) for x in line]
        valid, problem = check_values(line)
        # print(valid, problem, line)
        if not valid:
            line_1 = line[:]
            del line_1[problem]
            valid, _ = check_values(line_1)
        if not valid:
            line_2 = line[:]
            del line_2[problem+1]
            valid, _ = check_values(line_2)
        if valid:
            count += 1
            continue

    return count

def check_values(line):
    increasing = False
    decreasing = False
    problem = -1
    valid = True
    for i, v in enumerate(line):
        v2 = line[i+1] if i+1 < len(line) else None
        if not v2:
            break
        if v == line[i+1]:          
            # print('invalid equals:', line)
            valid = False
            problem = i
            break
        if i == 0:
            if v < v2 and not decreasing:
                increasing = True
            elif v > v2 and not increasing:
                decreasing = True
        if increasing and v > v2:
            # print('invalid inceasing:', line)
            valid = False
            problem = i
            break
        if decreasing and v < v2:
            # print('invalid decreasing:', line)
            valid = False
            problem = i
            break
        if abs(v - v2) > 3:
            # print('invalid difference:', line)
            valid = False
            problem = i
            break
    return valid, problem

if __name__ == '__main__':
    print(count_safe_reports('example_input.txt'))
line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]

def solution(line):
    num_line = len(line)
    ans_set = set()
    for i in range(num_line):
        for j in range(i+1, num_line):
            if (line[i][0]*line[j][1]-line[i][1]*line[j][0]) and (line[i][0]*line[j][1]-line[i][1]*line[j][0]):
                temp_x = (line[i][1]*line[j][2] - line[i][2]*line[j][1]) / (line[i][0]*line[j][1]-line[i][1]*line[j][0])
                temp_y = (line[i][2]*line[j][0]-line[i][0]*line[j][2]) / (line[i][0]*line[j][1]-line[i][1]*line[j][0])
                if int(temp_x) == temp_x and int(temp_y) == temp_y:
                    ans_set.add((int(temp_x), int(temp_y)))
    # print(ans_set)
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -float('inf'), -float('inf')
    for x, y in ans_set:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    # print(max_x - min_x + 1, max_y - min_y + 1, min_x, min_y)
    temp_answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in ans_set:
        # print(x-min_x, max_y-y)
        temp_answer[max_y - y][x - min_x] = '*'
    answer = []
    for inner in temp_answer:
        answer.append(''.join(inner))
    return answer

print(solution(line))
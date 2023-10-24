import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

graph = [[0] * 52 for _ in range(52)]
for _ in range(int(input())):
    string = input().rstrip()

    start = ord(string[0]) - ord('A')
    end = ord(string[-1]) - ord('A')

    if start >= 26:
        start -= 6
    if end >= 26:
        end -= 6

    graph[start][end] = 1


for k in range(52):
    for i in range(52):
        for j in range(52):
            if i == j:
                continue
            if not graph[i][j] and graph[i][k] and graph[k][j]:
                graph[i][j] = 1


ans_list = []
for i in range(52):
    for j in range(52):
        if i == j:
            continue

        if graph[i][j]:

            if i < 26:
                start = chr(i + 65)
            else:
                start = chr(i + 71)

            if j < 26:
                end = chr(j + 65)
            else:
                end = chr(j + 71)

            ans_list.append([start, end])


print(len(ans_list))
for start, end in ans_list:
    print(f'{start} => {end}')
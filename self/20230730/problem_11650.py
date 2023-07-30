N = int(input())
input_list = []

for _ in range(N):
    input_list.append(list(map(int, input().split())))

input_list.sort()

for i in input_list:
    print(*i)
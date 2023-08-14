N = int(input())
input_list = []

for _ in range(N):
    reverse_list = list(map(int, input().split()))
    reverse_list.reverse()
    input_list.append(reverse_list)

input_list.sort()

for i, j in input_list:
    print(j, i)
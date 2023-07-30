N = int(input())

input_list = []

for _ in range(N):
    input_list.append(str(input()))

input_list = set(input_list)
input_list = list(input_list)

ans_list = []

for i in input_list:
    num_and_str = [len(i), i]
    ans_list.append(num_and_str)

ans_list.sort()

for i, j in ans_list:
    print(j)
N = int(input())
empty_list = []

for _ in range(N):
    empty_list.append(int(input()))

empty_list.sort()

for i in empty_list:
    print(i)
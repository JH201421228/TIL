import sys
from collections import deque
# sys.stdin = open('input.txt')

input = sys.stdin.readline

N = int(input())
structure = list(map(int, input().split()))
init_list = deque([map(int, input().split())])
insert_num = int(input())
insert_list = list(map(int, input().split()))
return_list = []

for i in range(insert_num):
    input_num = insert_list[i]
    for j in range(N):
        if structure[j] == 0:
            init_list.insert(j, input_num)
            input_num = init_list.pop(j+1)

    return_list.append(input_num)

print(*return_list)




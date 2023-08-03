import sys
sys.stdin = open('input.txt')

input_list = list(map(int, input().split()))

length = len(input_list)
cnt = 0
for i in range(1, 1<<length):
    out_list = []
    for j in range(length):
        if i & (1<<j):
            out_list.append(input_list[j])
    cnt += 1
    print(out_list, cnt)

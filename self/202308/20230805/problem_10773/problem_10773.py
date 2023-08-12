import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline

K = int(input())
ans_lsit = []
for test_case in range(K):
    input_num = int(input())

    if input_num:
        ans_lsit.append(input_num)
    else:
        ans_lsit.pop()

print(sum(ans_lsit))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


count = [0] * 11
for _ in range(2047):
    temp = list(map(int, input().split()))
    for i in range(11):
        if temp[i]: count[i] += 1

ans_list = []
for n in count:
    if n == 1024:
        ans_list.append(0)
    else:
        ans_list.append(1)

print(*ans_list)
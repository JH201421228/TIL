import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


S = input().rstrip()

temp = S
for n in range(len(S)):
    temp = S

    for idx in range(n, 0, -1):
        temp += S[idx-1]

    mid = (len(S)+n) // 2

    for idx in range(mid):
        if temp[idx] != temp[-idx-1]: break

    else:
        break

print(len(S)+n)
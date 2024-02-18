import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


data = [[0 for _ in range(31)] for _ in range(31)]

for i in range(1, 31):
    data[i][0] = 1
for i in range(1, 31):
    data[i][i] = 1

for i in range(1, 31):
    for j in range(1, 31):
        if not data[i][j]:
            data[i][j] = data[i-1][j] + data[i-1][j-1]


def bino_coef():
    n, m = map(int, input().split())


    if n == m:
        print(1)
        return

    print(data[m][n])
    return

for _ in range(int(input())):
    bino_coef()
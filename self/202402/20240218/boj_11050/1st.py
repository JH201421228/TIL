import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def bino_coef():
    n, k = map(int, input().split())
    data = [[0 for _ in range(k+1)] for _ in range(n+1)]
    # n개중 k를 고르는 경우의 수 모두 저장할 배열 생성

    if not k or k == n:
        print(1)
        return
    # 경우의 수가 1인 경우 처리

    for i in range(1, n+1):
        data[i][0] = 1
    for i in range(1, k+1):
        data[i][i] = 1
    # 이항계수의 기본 성질

    for i in range(1, n+1):
        for j in range(1, k+1):
            if not data[i][j]:
                data[i][j] = data[i-1][j] + data[i-1][j-1]

    print(data[n][k])

bino_coef()

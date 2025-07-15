import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())

    matrix = [[0] * (N+1) for _ in range(21)]
    for i in range(1, N+1):
        matrix[len(input().rstrip())][i] = 1

    for col in range(1, 21):
        for row in range(1, N+1):
            matrix[col][row] += matrix[col][row-1]

    res = 0
    for col in range(1, 21):
        for row in range(1, N+1):
            if matrix[col][row] != matrix[col][row-1]:
                if row+K > N: res += matrix[col][N] - matrix[col][row]
                else: res += matrix[col][row+K] - matrix[col][row]

    print(res)

    return


if __name__ == "__main__":
    solve()
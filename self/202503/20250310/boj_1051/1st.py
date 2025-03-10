import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())
G = [list(map(int, list(input().rstrip()))) for _ in range(N)]

minn = min(N, M)

for n in range(minn, 1, -1):
    for i in range(N-n+1):
        for j in range(M-n+1):
            if G[i][j] == G[i][j+n-1] and G[i][j] == G[i+n-1][j] and G[i][j] == G[i+n-1][j+n-1]:
                print(n**2)
                exit(0)

print(1)
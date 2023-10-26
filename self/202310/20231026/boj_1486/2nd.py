import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


N, M, T, D = map(int, input().split())
mountain = [list(input().rstrip()) for _ in range(N)]
# print(mountain)
for i in range(N):
    for j in range(M):
        num = ord(mountain[i][j]) - ord('A')
        if num > 25:
            num -= 6
        mountain[i][j] = num

for inner in mountain:
    print(inner)


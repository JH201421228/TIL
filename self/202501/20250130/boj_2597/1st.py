import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

L = int(input())
D = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    if D[i][0] == D[i][1]:
        continue
    mid = (D[i][0] + D[i][1]) / 2
    L = max(L - mid, mid)

    for j in range(i+1, 3):
        D[j] = [abs(mid - D[j][0]), abs(mid - D[j][1])]

print(f"{L:.1f}")
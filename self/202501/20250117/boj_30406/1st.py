import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def greedy(a, b):
    global ans

    temp = min(C[a], C[b])
    ans += temp * (a^b)
    C[a] -= temp
    C[b] -= temp

    return

N = int(input())
G = list(map(int, input().split()))
C = [0, 0, 0, 0]

for n in G:
    C[n] += 1

ans = 0
idxs = [(0, 3), (1, 2), (0, 2), (1, 3), (0, 1), (2, 3)]

for i, j in idxs:
    greedy(i, j)

print(ans)
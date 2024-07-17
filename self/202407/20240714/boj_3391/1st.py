import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]

for i in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in temp[1:]:
        G[i].append(j)

order = list(map(int, input().split()))
order_dict = dict()

for i in range(1, N+1):
    order_dict[order[i-1]] = i

print(order_dict)
order.sort(reverse=True)
C = [0] * (N+1)
for i in range(1, N+1):
    V = [0] * (N+1)
    B(order_dict[order[i-1]])

print(C)
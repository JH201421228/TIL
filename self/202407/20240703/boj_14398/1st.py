import sys, math
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


N = map(int, input().split())
temp = list(map(int, input().split()))
O, E = [0], [0]

for v in temp:
    if v%2:
        O.append(v)
    else:
        E.append(v)

l_o, l_e = len(O)-1, len(E)-1

G = [[] for _ in range(l_o+1)]
C = [0] * (l_e+1)

for i in range(1, l_o+1):
    for j in range(1, l_e+1):
        if math.gcd(O[i], E[j]) == 1 and (O[i]**2 + E[j]**2)**0.5 == int((O[i]**2 + E[j]**2)**0.5):
            G[i].append(j)

ans = 0
for i in range(1, l_o+1):
    V = [0] * (l_e+1)
    if B(i):
        ans += 1

print(ans)
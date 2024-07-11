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


I = list(map(str, input().rstrip()))
for idx in range(len(I)):
    if ord(I[idx]) <= 90:
        I[idx] = ord(I[idx])-64
    else:
        I[idx] = ord(I[idx])-96+26

G = [[] for _ in range(26*2+1)]
C = [0] * (26*2+1)

for idx in range(len(I)-1):
    if I[idx] <= 26 and I[idx+1] >= 27:
        G[I[idx]].append(I[idx+1])
    elif I[idx+1] <= 26 and I[idx] >= 27:
        G[I[idx]].append(I[idx + 1])

ans = 0
for i in range(1, 26*2+1):
    V = [0] * (26*2+1)
    if B(i):
        ans += 1

check_list = []

for idx in range(1, 26*2+1):
    if C[idx]:
        check_list.append((C[idx], idx))

check = [0] * len(I)


for idx in range(len(I)-1):
    for n1, n2 in check_list:
        if I[idx] == n1 and I[idx+1] == n2:
            check[idx] += 1
            check[idx+1] += 1

for idx in range(len(I)-1):
    isNotUseful = True
    for n1, n2 in check_list:
        if I[idx] == n1 and I[idx+1] == n2:
            if check[idx] == 1 or check[idx+1] == 1:
                isNotUseful = False
                break

    if isNotUseful:
        ans -= 1
print()
print(check_list)
print(I)
print(check)
print(ans)


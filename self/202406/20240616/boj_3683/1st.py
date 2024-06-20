import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if Vi[x]:
            continue
        Vi[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


for _ in range(int(input())):
    C, D, V = map(int, input().split())
    CAT, DOG = [], []
    for _ in range(V):
        a, b = map(str, input().rstrip().split())
        if a[0] == 'C':
            CAT.append((a, b))
        else:
            DOG.append((a, b))

    n_c, n_d = len(CAT), len(DOG)
    G = [[] for _ in range(n_c+1)]
    C = [0] * (n_d+1)

    for i in range(n_c):
        for j in range(n_d):
            if CAT[i][0] == DOG[j][1] or CAT[i][1] == DOG[j][0]:
                G[i+1].append(j+1)

    ans = 0
    for i in range(1, n_c+1):
        Vi = [0] * (n_d+1)
        if B(i):
            ans += 1

    print(V-ans)
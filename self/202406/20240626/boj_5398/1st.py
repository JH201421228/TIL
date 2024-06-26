import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(500)


def B(n):
    for x in G[n]:
        if W[x]:
            continue
        W[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


for _ in range(int(input())):
    H, V = map(int, input().split())

    G1, G2 = [[0] * (2_001) for _ in range(2_001)], [[0] * (2_001) for _ in range(2_001)]

    for i in range(1, H+1):
        temp = list(map(str, input().rstrip().split()))
        l = len(temp[2])

        for j in range(int(temp[0]), int(temp[0])+l):
            G1[int(temp[1])][j] = temp[2][j-int(temp[0])]
            G2[int(temp[1])][j] = i

    G = [[] for _ in range(H+1)]
    C = [0] * (V+1)

    for i in range(1, V+1):
        temp = list(map(str, input().rstrip().split()))
        l = len(temp[2])

        for j in range(int(temp[1]), int(temp[1])+l):
            if G1[j][int(temp[0])] and G1[j][int(temp[0])] != temp[2][j-int(temp[1])]:
                G[G2[j][int(temp[0])]].append(i)

    ans = H + V

    for i in range(1, H+1):
        W = [0] * (V+1)
        if B(i):
            ans -= 1

    print(ans)
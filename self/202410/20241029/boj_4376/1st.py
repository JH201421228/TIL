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

while True:
    try:
        N, M, S, V = map(int, input().split())
        gopers = [[]]
        holes = [[]]

        for _ in range(N):
            gopers.append(tuple(map(float, input().split())))

        for _ in range(M):
            holes.append(tuple(map(float, input().split())))

        G = [[] for _ in range(N+1)]

        for i in range(1, N+1):
            g_x, g_y = gopers[i]

            for j in range(1, M+1):
                h_x, h_y = holes[j]

                if ((g_x-h_x)**2+(g_y-h_y)**2)**0.5 <= S*V:
                    G[i].append(j)

        ans = 0
        C = [0] * (M+1)
        for i in range(1, N+1):
            V = [0] * (M+1)
            B(i)

        for i in range(1, M+1):
            if C[i]:
                ans += 1

        print(N-ans)

    except:
        break
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(N, M, G):
    distance = [float('inf')] * (N+1)
    distance[1] = 0

    for i in range(N):
        for j in range(M):
            u, v, c = G[j]

            if distance[v] > distance[u] + c:
                distance[v] = distance[u] + c

                if i == N-1:
                    return False

    return distance


def main():
    N, M = map(int, input().split())

    G = []
    for _ in range(M):
        G.append(tuple(map(int, input().split())))

    ans = solve(N, M, G)
    if ans:
        for i in ans[2:]:
            if i != float('inf'):
                print(i)
            else:
                print(-1)
    else:
        print(-1)

    return


if __name__ == "__main__":
    main()
import sys
from itertools import product
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


deltas = [((1, 0), (-1, 0)), ((0, 1), (0, -1)), ((1, 1), (-1, -1)), ((1, -1), (-1, 1))]


def get_score(state, N, M):
    score = [0, 0, 0]
    for i in range(N):
        for j in range(M):
            link = 0
            for delta in deltas:
                tmp = 1
                q = deque([(i, j)])
                V = [[0] * M for _ in range(N)]
                V[i][j] = 1

                while q:
                    ni, nj = q.popleft()
                    for di, dj in delta:
                        xi, xj = ni+di, nj+dj
                        if xi >= 0 and xi < N and xj >= 0 and xj < M and not V[xi][xj] and state[xi][xj] == state[i][j]:
                            V[xi][xj] = 1
                            q.append((xi, xj))
                            tmp += 1

                    if tmp > 3:
                        tmp = min(4, tmp)
                        break

                link = max(link, tmp)
                if link == 4: break

            if link > 1: score[link-2] += 1

    return score


def solve():
    N, M, K, S4, S3, S2 = map(int, input().split())

    init_state = [list(input().rstrip()) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if init_state[i][j] == '?': cnt += 1

    pros = list(product([n for n in range(1, K+1)], repeat=cnt))
    ans = 0
    for pro in pros:
        idx = 0
        temp = [[] for _ in range(N)]
        for i in range(N):
            for j in range(M):
                if init_state[i][j] == '?':
                    temp[i].append(pro[idx])
                    idx += 1
                else:
                    temp[i].append(int(init_state[i][j]))

        score = get_score(temp, N, M)
        ans += score[0] * S2
        ans += score[1] * S3
        ans += score[2] * S4

    return ans / len(pros)


def init():
    for i in range(int(input())):
        print(f"Case #{i+1}: {solve()}")

    return


if __name__ == "__main__":
    init()
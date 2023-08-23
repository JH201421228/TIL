import sys
sys.stdin = open('input.txt')


def cordinate_maker(K):
    ans = []
    for i in range(-K + 1, K):
        for j in range(-K + 1 + abs(i), K - abs(i)):
            ans.append([i, j])
    return ans


def cost(N, M, K):

    max_home = 0
    cordinates = cordinate_maker(K)
    for i in range(N):
        for j in range(N):
            cnt = 0
            for di, dj in cordinates:
                if 0 <= i+di < N and 0 <= j+dj < N and home_info[i+di][j+dj]:
                    cnt += 1
            if cnt > max_home:
                max_home = cnt

    service_cost = K ** 2 + (K - 1) ** 2
    customer_cost = max_home * M
    if customer_cost >= service_cost:
        return max_home
    else:
        return False


Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    home_info = [list(map(int, input().split())) for _ in range(N)]
    for K in range(N+1, 0, -1):
        if cost(N, M, K):
            print(f'#{test+1} {cost(N, M, K)}')
            break
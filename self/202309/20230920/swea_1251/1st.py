import sys
sys.stdin = open('input.txt')


def this_problem_is_suck(val, x, y, num):
    global ans
    if num == N:
        if val < ans:
            ans = val
            return

    if val > ans:
        return

    for idx in range(1, N):
        if not island[idx]:
            island[idx] = 1
            x_, y_ = cordinate_info[0][idx], cordinate_info[1][idx]
            this_problem_is_suck(val + ((x_ - x) ** 2 + (y_ - y) ** 2), x_, y_, num + 1)
            island[idx] = 0


T = int(input())
for test in range(T):
    N = int(input())
    cordinate_info = [list(map(int, input().split())) for _ in range(2)]
    E = float(input())
    # print(cordinate_info)
    # print(E)
    island = [0] * N
    island[0] = 1
    ans = float('inf')
    this_problem_is_suck(0, 0, 0, 1)
    print(f'#{test+1} {ans * E}')
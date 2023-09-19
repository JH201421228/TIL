import sys
sys.stdin = open('input.txt')


def this_problem_is_shit(i_idx, val):
    global ans

    if i_idx == N:
        if ans < val:
            ans = val
        return

    if val <= ans:
        return

    for j in range(N):
        if not trace[j]:
            trace[j] = 1
            this_problem_is_shit(i_idx + 1, val * (work_sche[i_idx][j]/100))
            trace[j] = 0


T = int(input())
for test in range(T):
    N = int(input())
    work_sche = [list(map(int, input().split())) for _ in range(N)]
    # print(work_sche)
    ans = 0
    trace = [0] * N
    this_problem_is_shit(0, 1)
    print(f'#{test+1} {100 * ans:.6f}')
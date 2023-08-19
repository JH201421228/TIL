import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)


def how_many_change(M):
    change_cnt = 0
    for i in range(arr[1]):
        for j in range(M):
            if flag[i][j] != 'W':
                change_cnt += 1
    for i in range(arr[1], arr[1] + arr[2]):
        for j in range(M):
            if flag[i][j] != 'B':
                change_cnt += 1
    for i in range(arr[1] + arr[2], sum(arr)):
        for j in range(M):
            if flag[i][j] != 'R':
                change_cnt += 1
    ans.append(change_cnt)


def three_num(N, M):
    if len(arr) == 3 and sum(arr) == N:
        how_many_change(M)
        return
    if len(arr) == 3:
        return
    if sum(arr) > N:
        return

    for i in range(1, N-1):
        arr.append(i)
        three_num(N, M)
        arr.pop()


Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    flag = [list(map(str, input())) for _ in range(N)]
    arr = []
    ans = []
    three_num(N, M)
    print(f'#{test + 1} {min(ans)}')
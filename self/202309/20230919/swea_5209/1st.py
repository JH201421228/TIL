import sys
sys.stdin = open('input.txt')


def why_do_this(row, val):
    global ans

    if row == N:
        if ans > val:
            ans = val
        return

    if val >= ans:
        return

    for j in range(N):
        if not trace[j]:
            trace[j] = 1
            why_do_this(row+1, val+product_line[row][j])
            trace[j] = 0



T = int(input())
for test in range(T):
    N = int(input())
    product_line = [list(map(int, input().split())) for _ in range(N)]
    # 겹치는 라인이 없게 라인 정보를 넣을 리스트 생성
    # 최소값으로 가지치기 ㄱㄱ
    trace = [0] * N
    ans = 100 * N
    why_do_this(0, 0)
    print(f'#{test+1} {ans}')

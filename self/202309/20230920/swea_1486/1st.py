import sys
sys.stdin = open('input.txt')


def dua_lipa_IDGAF(start, val):
    if val >= B:
        global ans
        if val < ans:
            ans = val
        return

    for idx in range(start, N):
        dua_lipa_IDGAF(idx+1, val+height_list[idx])


T = int(input())
for test in range(T):
    N, B = map(int, input().split())
    height_list = sorted(list(map(int, input().split())))
    # print(height_list)
    ans = 10_000 * 20
    dua_lipa_IDGAF(0, 0)
    print(f'#{test + 1} {ans - B}')
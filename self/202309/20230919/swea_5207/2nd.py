import sys
sys.stdin = open('input.txt')

def binary_search(find_num, start, end, status, ans):

    if start > end:
        return ans

    mid = (start + end) // 2

    if N_list[mid] == find_num:
        ans += 1

    elif N_list[mid] < find_num:
        if status == 1:
            return ans
        ans = binary_search(find_num, mid+1, end, 1, ans)

    else:
        if status == -1:
            return ans
        ans = binary_search(find_num, start, mid-1, -1, ans)

    return ans

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = list(map(int, input().split()))
    ans = 0
    for num in M_list:
        ans = binary_search(num, 0, N-1, 0, ans)
    print(f'#{test+1} {ans}')

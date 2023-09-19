import sys
sys.stdin = open('input.txt')


def partition(start, end):

    if start >= end:
        return

    pivot = start
    left, right = start + 1, end

    while left <= right:
        while left <= end and plz_sort[pivot] >= plz_sort[left]:
            left += 1
        while start < right and plz_sort[pivot] < plz_sort[right]:
            right -= 1

        if left > right:
            plz_sort[start], plz_sort[right] = plz_sort[right], plz_sort[start]
        else:
            plz_sort[left], plz_sort[right] = plz_sort[right], plz_sort[left]

    partition(start, right - 1)
    partition(right + 1, end)


T = int(input())
for test in range(T):
    N = int(input())
    plz_sort = list(map(int, input().split()))
    partition(0, len(plz_sort) - 1)
    print(f'#{test+1} {plz_sort[N//2]}')


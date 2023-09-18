import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)


def someones_partition(left, right):
    pivot = sort_plz[left]
    left += 1

    while True:
        while sort_plz[left] <= pivot:
            left += 1
        while sort_plz[right] > pivot:
            right -= 1

        if left >= right:
            return right

        sort_plz[left], sort_plz[right] = sort_plz[right], sort_plz[left]


def is_it_real_quick_sort(left, right):
    if left >= right:
        return
    pivot = someones_partition(left, right)
    sort_plz[left], sort_plz[pivot] = sort_plz[pivot], sort_plz[left]

    is_it_real_quick_sort(left, pivot)
    is_it_real_quick_sort(pivot + 1, right)


T = int(input())
for test in range(T):
    N = int(input())
    sort_plz = list(map(int, input().split()))
    # print(sort_plz)
    is_it_real_quick_sort(0, len(sort_plz)-1)
    print(sort_plz)
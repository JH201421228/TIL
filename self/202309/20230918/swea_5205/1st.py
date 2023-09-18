import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

def someones_partition(left, right):
    pivot = sort_plz[left]
    low = left + 1
    high = right

    while True:
        while low <= high and sort_plz[low] <= pivot:
            low += 1
        while low <= high and sort_plz[high] > pivot:
            high -= 1

        if low <= high:
            sort_plz[low], sort_plz[high] = sort_plz[high], sort_plz[low]
        else:
            break

    sort_plz[left], sort_plz[high] = sort_plz[high], sort_plz[left]
    return high

def is_it_real_quick_sort(left, right):
    if left < right:
        pivot = someones_partition(left, right)
        is_it_real_quick_sort(left, pivot - 1)
        is_it_real_quick_sort(pivot + 1, right)

T = int(input())
for test in range(T):
    N = int(input())
    sort_plz = list(map(int, input().split()))
    is_it_real_quick_sort(0, len(sort_plz) - 1)
    print(f'#{test+1} {sort_plz[N//2]}')
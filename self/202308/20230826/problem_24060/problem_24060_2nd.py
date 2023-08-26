import sys
sys.stdin = open('input.txt')


def merge_sort(ar):
    if len(ar) == 1:
        return ar

    mid = (len(ar) + 1) // 2
    left = merge_sort(ar[:mid])
    right = merge_sort(ar[mid:])

    arrr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arrr.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            arrr.append(right[j])
            ans.append(right[j])
            j += 1

    while i < len(left):
        arrr.append(left[i])
        ans.append(left[i])
        i += 1

    while j < len(right):
        arrr.append(right[j])
        ans.append(right[j])
        j += 1

    return arrr


A, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
merge_sort(arr)
if len(ans) >= K:
    print(ans[K-1])
else:
    print(-1)
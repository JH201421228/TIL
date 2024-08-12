import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def merge(s, e):
    global ans

    mid = (s+e) // 2
    i = s
    j = mid + 1
    k = s
    cnt = 0

    while (i <= mid and j <= e):
        if (arr[i] <= arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
            ans += cnt
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            cnt += 1

    if (i > mid):
        ss = j
        while (ss <= e):
            temp[k] = arr[ss]
            k += 1
            ss += 1

    else:
        ss = i
        while (ss <= mid):
            temp[k] = arr[ss]
            k += 1
            ss += 1
            ans += cnt

    for idx in range(s, e+1):
        arr[idx] = temp[idx]


def mergesort(s, e):
    if (s < e):
        mid = (s+e) // 2
        mergesort(s, mid)
        mergesort(mid+1, e)
        merge(s, e)



N = int(input())
arr = list(map(int, input().split()))
temp = [0] * len(arr)
ans = 0

mergesort(0, N-1)
print(ans)

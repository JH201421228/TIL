import sys
sys.stdin = open('input.txt')

# ############절취선#################

def binarySearch(a, N, key):
    start = 0
    end = N - 1
    while start <= end:
        mid = (end + start) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            end = mid - 1
        elif a[mid] < key:
            start = mid + 1

    return False

# ############절취선#################

arr = list(map(int, input().split()))
print(binarySearch(arr, len(arr), 23))
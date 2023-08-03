# def binary_search(arr, N, key):
#     start = 0
#     end = N-1
#     while start <= end:
#         mid = (end + start)//2
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] > key:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return False

def binary_search(arr, N, key, start, end):
    if start > end:
        return False
    else:
        mid = (start + end)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid-1
            return binary_search(arr, N, key, start, end)
        else:
            start = mid+1
            return binary_search(arr, N, key, start, end)

numbers = list(range(1, 30, 2))
print(numbers)
N = len(numbers)
target = 25
# 이진 탐색

print(binary_search(numbers, N, target, 0, N-1))
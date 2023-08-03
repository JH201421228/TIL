import sys
sys.stdin = open('input.txt')

def select_sort(arr, N):
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

input_list = list(map(int, input().split()))

print(select_sort(input_list, len(input_list)))
import sys
sys.stdin = open('input.txt')

input_list = list(map(int, input().split()))

def bubble_sort(arr):
    length = len(arr)
    for i in range(1, length):
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort(input_list))
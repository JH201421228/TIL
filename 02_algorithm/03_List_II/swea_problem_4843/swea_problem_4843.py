import sys
sys.stdin = open('input.txt')

def odd_sort(arr):
    n = len(arr)
    for i in range(n-1):

        if i % 2:
            min_index = i
            for j in range(i+1, n):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]

        else:
            max_index = i
            for j in range(i+1, n):
                if arr[max_index] < arr[j]:
                    max_index = j
            arr[i], arr[max_index] = arr[max_index], arr[i]

    return arr


Test_Case = int(input())

for test_case in range(Test_Case):
    num_of_num = int(input())
    check_list = list(map(int, input().split()))
    print(f'#{test_case+1}', end=' ')
    ans_list = odd_sort(check_list)
    for i in range(10):
        print(ans_list[i], end=' ')
    print()
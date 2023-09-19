import sys
sys.stdin = open('input.txt')


def merge_plz(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    front_list = merge_plz(arr[:mid])
    rear_list = merge_plz(arr[mid:])

    global ans

    return_list = []
    low = high = 0
    if front_list[-1] > rear_list[-1]:
        ans += 1

    while low < len(front_list) and high < len(rear_list):

        if front_list[low] < rear_list[high]:
            return_list.append(front_list[low])
            low += 1
        else:
            return_list.append(rear_list[high])
            high += 1

    return_list.extend(front_list[low:])
    return_list.extend(rear_list[high:])

    return return_list

T = int(input())
for test in range(T):
    N = int(input())
    plz_sort = list(map(int, input().split()))
    ans = 0
    print(f'#{test+1} {merge_plz(plz_sort)[N//2]} {ans}')
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

def find_min_list_size(S, P):
    if S == P:
        return 1

    n_1 = int(S // math.e)
    n_2 = n_1 + 1

    if n_1 and S / n_1 >= P ** (1 / n_1):
        start, end = 2, n_1
        while start <= end:
            mid = (start + end) >> 1
            if S / mid <= P ** (1 / mid):
                start = mid + 1
            else:
                end = mid - 1
        return start
    elif S / n_2 >= P ** (1 / n_2):
        return n_2
    else:
        return -1

S, P = map(int, input().split())
print(find_min_list_size(S, P))

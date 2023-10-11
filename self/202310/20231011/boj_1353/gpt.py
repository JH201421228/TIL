import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline

# mid일 때 p 이상
# mid - 1일 때 p 이하
def search():
    start = 2
    end = max_x2

    while start <= end:
        mid = (start + end) // 2
        val = math.pow(S / mid, mid)
        val_prime = math.pow(S / (mid - 1), mid - 1)

        if val >= P and val_prime < P:
            return mid
        elif val_prime >= P:
            end = mid - 1
        elif val < P:
            start = mid + 1
    return mid

S, P = map(int, input().split())

max_x1 = S / math.e
max_x2 = S // math.e + 1

if S == P:
    print(1)
elif (S / max_x1) ** max_x1 < P:
    print(-1)
else:
    n = 2
    print(int(search()))

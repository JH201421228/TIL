import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


check_dict = {
    (1, 3): 2,
    (3, 1): 2,
    (4, 6): 5,
    (6, 4): 5,
    (7, 9): 8,
    (9, 7): 8,
    (1, 7): 4,
    (7, 1): 4,
    (2, 8): 5,
    (8, 2): 5,
    (3, 9): 6,
    (9, 3): 6,
    (1, 9): 5,
    (9, 1): 5,
    (3, 7): 5,
    (7, 3): 5,
}

L = int(input())
arr = list(map(int, input().split()))

for idx in range(1, L):
    if ((arr[idx-1], arr[idx]) in check_dict and check_dict[(arr[idx-1], arr[idx])] not in arr[:idx+1]) or (arr[idx] in arr[:idx]):
        print("NO")
        break
else:
    print("YES")
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
B.sort()

A_dict = dict()
B_dict = dict()

for idx in range(N):

    ans = 0
    start, end = 0, N-1
    while start < end:
        if start == idx:
            start += 1
        elif end == idx:
            end -= 1

        if start == end:
            continue

        sum_val = A[start] + A[end]
        if sum_val == A[idx]:
            A_dict[A[idx]] = A_dict.get(A[idx], 0) + 1
            if abs(A[start] + A[end-1] - sum_val) > abs(A[start+1] + A[end] - sum_val):
                start += 1
            else:
                end -= 1

        elif sum_val > A[idx]:
            end -= 1
        else:
            start += 1
print(A_dict)

for idx in range(M):

    ans = 0
    start, end = 0, M-1
    while start < end:
        if start == idx:
            start += 1
        elif end == idx:
            end -= 1

        if start == end:
            continue

        sum_val = B[start] + B[end]
        if sum_val == B[idx]:
            B_dict[B[idx]] = B_dict.get(B[idx], 0) + 1
            if abs(B[start] + B[end-1] - sum_val) > abs(B[start+1] + B[end] - sum_val):
                start += 1
            else:
                end -= 1

        elif sum_val > B[idx]:
            end -= 1
        else:
            start += 1
print(B_dict)

ans = 0
for n in A:
    for m in B:
        if n + m == T:
            ans += (A_dict.get(n, 0) + 1) * (B_dict.get(m, 0) + 1)
print(ans)

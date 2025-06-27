import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def median_of_medians(A, k):
    if len(A) <= 5:
        return sorted(A)[k - 1]

    sublists = [A[i:i+5] for i in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    median_of_median = median_of_medians(medians, (len(medians)+1)//2)

    low = [x for x in A if x < median_of_median]
    high = [x for x in A if x > median_of_median]

    rank = len(low) + 1

    if k == rank:
        return median_of_median
    elif k < rank:
        return median_of_medians(low, k)
    else:
        return median_of_medians(high, k - rank)

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        _, i, j, k = query
        subset = A[i-1:j]
        print(median_of_medians(subset, k))

    elif query[0] == 2:
        _, i, j = query
        A[i-1], A[j-1] = A[j-1], A[i-1]
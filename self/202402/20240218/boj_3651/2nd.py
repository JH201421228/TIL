import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


m = int(input())


def bino_coef(n, k):
    ans = 1
    for i in range(0, k):
        ans *= (n-i)
    for i in range(0, k):
        ans //= (i+1)
    return ans

ans_list = []
for i in range(1, 61):
    start, end = i, m+1
    while start + 1 < end:
        mid = (start+end)//2
        if bino_coef(mid, i) <= m:
            start = mid
        else:
            end = mid
    if bino_coef(start, i) == m:
        ans_list.append((start, i))
        # if i < start - i:
        #     ans_list.append((start, start-i))
ans_list.sort(key=lambda x: (x[0], x[1]))
print(len(ans_list))
for inner in ans_list:
    print(*inner)
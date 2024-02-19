import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, k, m = map(int, input().split())

def bino_coef(n, k):

    if k > n:
        return 0
    if k == 0:
        return 1
    if k == n:
        return 1

    ans = 1
    for i in range(k):
        ans *= (n-i)
    for i in range(k):
        ans //= (i+1)
    return ans

def lucas_arr(n, k):
    arr1 = []
    arr2 = []
    while n or k:
        arr1.append(n%m)
        arr2.append(k%m)
        n //= m
        k //= m

    return arr1, arr2

arr1, arr2 = lucas_arr(n, k)

ans = 1
for i in range(len(arr1)):
    ans *= bino_coef(arr1[i], arr2[i])
print(ans%m)
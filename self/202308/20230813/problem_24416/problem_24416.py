import sys
# sys.stdin = open('input.txt')

def fib1(n):
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        cnt1 -= 1
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n):
    global cnt2

    f = [0] * (n+1)
    f[1] = f[2] = 1
    for i in range(3, n+1):
        cnt2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


cnt1 = 1
cnt2 = 0
n = int(input())
fib1(n)
fib2(n)
print(cnt1, cnt2)
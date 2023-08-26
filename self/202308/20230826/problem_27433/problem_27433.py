import sys
sys.stdin = open('input.txt')


def fibo(n):
    if not n:
        return 1
    return n*fibo(n-1)

N = int(input())
print(fibo(N))
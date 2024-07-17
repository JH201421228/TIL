import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isPrime(n):
    for i in range(2, int(n**0.5+1)):
        if prime[i] and not n%i:
            return False

    return True


# def B(n):
#     for x in G[n]:
#         if V[x]:
#             continue
#         V[x] = 1
#
#         if not C[x] or B(C[x]):
#             C[x] = n
#             return True
#
#     return False


N, M = map(int, input().split())
potions = [0] + list(map(int, input().split()))

prime = [1] * int(N**0.5+1)

for i in range(2, int(N**0.5+1)):
    if prime[i]:
        for j in range(i**2, int(N**0.5+1), i):
            prime[j] = 0
import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve(N):

    if N == 1:
        print(1)
        return

    V = [0] * N
    V[1] = 1
    q = deque([1])

    while q:
        n = q.popleft()

        if not (n * 10) % N:
            print(n * 10)
            return
        else:
            if not V[(n * 10) % N]:
                V[(n * 10) % N] = 1
                q.append((n * 10))

        if not (n * 10 + 1) % N:
            print(n * 10 + 1)
            return
        else:
            if not V[(n * 10 + 1) % N]:
                V[(n * 10 + 1) % N] = 1
                q.append((n * 10 + 1))

    return

def init():
    while True:
        N = int(input())

        if N: solve(N)
        else: break


if __name__ == "__main__":
    init()
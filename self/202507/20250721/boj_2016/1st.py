import sys
from collections import deque
from itertools import permutations
sys.stdin = open('input.txt')
input = sys.stdin.readline


def matching(mans, womans):
    q = deque([1, 2, 3, 4, 5])

    order = [0] * 5
    match = [0] * 5

    while q:
        xf = q.popleft()
        order[xf-1] += 1
        m = womans[xf-1][order[xf-1]-1]
        nf = match[m-1]
        if not nf: match[m-1] = xf
        elif mans[m-1].index(xf+5) < mans[m-1].index(nf+5):
            q.append(nf)
            match[m-1] = xf
        else:
            q.append(xf)

    return match[0]


def init():
    for _ in range(int(input())):
        if solve(): print("YES")
        else: print("NO")


def solve():
    mans = [[6, 7, 8, 9, 10]]
    for _ in range(4):mans.append(list(map(int, input().split())))
    womans = [list(map(int, input().split())) for _ in range(5)]

    first = matching(mans, womans)

    for permute in permutations([6, 7, 8, 9, 10], 5):
        mans[0] = permute
        if matching(mans, womans) < first:
            return 1

    return 0


if __name__ == "__main__":
    init()
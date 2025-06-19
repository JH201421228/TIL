import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 0123 cdhs
def isFlush(cards):
    for idx in range(4):
        if cards[idx][-1] == 5:
            return True
    return False


def isQuadruple(cards):
    for idx in range(1, 14):
        if cards[-1][idx] == 4:
            return True

    return False


def isStraight(cards):
    for s in range(1, 14):
        for ds in range(5):
            ss = s+ds
            if ss > 13: ss -= 13
            if cards[-1][ss] != 1: break
        else: return True

    return False


def isTriple(cards):
    for idx in range(1, 14):
        if cards[-1][idx] == 3:
            return True

    return False


def isTwoPair(cards):
    cnt = 0
    for idx in range(1, 14):
        if cards[-1][idx] == 2: cnt += 1

    if cnt == 2: return True
    return False


def isPair(cards):
    for idx in range(1, 14):
        if cards[-1][idx] == 2:
            return True

    return False


def isStraightFlush(cards):
    if isStraight(cards) and isFlush(cards):
        return True

    return False


def isFullHouse(cards):
    if isTriple(cards) and isPair(cards):
        return True

    return False


def checker(cards):
    if isStraightFlush(cards): return 0
    if isQuadruple(cards): return 1
    if isFullHouse(cards): return 2
    if isFlush(cards): return 3
    if isStraight(cards): return 4
    if isTriple(cards): return 5
    if isTwoPair(cards): return 6
    if isPair(cards): return 7

    return 8


def solve():
    cards = [[0] * 15 for _ in range(5)]
    for _ in range(4):
        p, n = map(int, input().split())
        cards[p][n] = 1
        cards[4][n] += 1
        cards[p][14] += 1

    ans = {i: [] for i in range(9)}

    for i in range(4):
        for j in range(1, 14):
            if not cards[i][j]:
                cards[i][j] = 1
                cards[4][j] += 1
                cards[i][14] += 1

                ans[checker(cards)].append((i, j))

                cards[i][j] = 0
                cards[4][j] -= 1
                cards[i][14] -= 1

    for k in range(9):
        if ans[k]:
            print(*ans[k][0])
            break

    return


if __name__ == "__main__":
    solve()
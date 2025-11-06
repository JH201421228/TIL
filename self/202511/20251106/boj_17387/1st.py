import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# 겹치는게 있으면 바로 출력
# 겹치는게 없으면 교차 판정하기

def isOnLine(l, p):
    if p[0] > min(l[0], l[2]) and p[0] < max(l[0], l[2]) and p[1] > min(l[1], l[3]) and p[1] < max(l[1], l[3]):
        if (l[0] - p[0]) * (l[3] - p[1]) == (l[1] - p[1]) * (l[2] - p[0]): return True

    return False

def crossCheck(p1, p2, p3):
    x21, y21, x32, y32 = p2[0] - p1[0], p2[1] - p1[1], p3[0] - p2[0], p3[1] - p2[1]

    return x21 * y32 - x32 * y21

def isInclude(l1, l2):
    if l1[:2] == l2[:2] or l1[:2] == l2[2:] or l1[2:] == l2[:2] or l1[2:] == l2[2:]: return True

    if isOnLine(l1, l2[:2]) or isOnLine(l1, l2[2:]) or isOnLine(l2, l1[:2]) or isOnLine(l2, l1[2:]): return True

    if crossCheck(l1[:2], l1[2:], l2[:2]) * crossCheck(l1[:2], l1[2:], l2[2:]) < 0 and crossCheck(l2[:2], l2[2:], l1[:2]) * crossCheck(l2[:2], l2[2:], l1[2:]) < 0: return True

    return False


def solve():
    lines = list(tuple(map(int, input().split())) for _ in range(2))

    if isInclude(lines[0], lines[1]): print(1)
    else: print(0)


def main():
    solve()

    return


if __name__ == "__main__":
    solve()
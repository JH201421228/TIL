import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def init():
    while True:
        B, P = map(int, input().split())
        if not B and not P: break

        print(solve(-B, P))
    return


def solve(B, P):
    info = []
    for _ in range(B):
        a, b = map(int, input().split())
        info.append([a, b, 0, 0])

    arr = [0] * (B+1)
    arr[0] = P

    res = 0

    while arr[-1] != P:
        res += 1

        for idx, (capa, time, cur, val) in enumerate(info):
            if arr[idx]:
                if cur == time-1:
                    arr[idx] -= val
                    arr[idx+1] += val
                    info[idx][2] = 0
                elif not cur:
                    info[idx][3] = min(arr[idx], capa)
                    info[idx][2] += 1
                else:
                    info[idx][2] += 1

    return res + B - 1


if __name__ == "__main__":
    init()
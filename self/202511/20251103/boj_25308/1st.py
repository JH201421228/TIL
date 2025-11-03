import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

unit = [(0, 2**.5), (1, 1), (2**.5, 0), (1, -1), (0, -2**.5), (-1, -1), (-2**.5, 0), (-1, 1)]
S = []
hexs = []

def isAvailable(scores, cur_state):
    for idx in range(8):
        x1, y1 = unit[idx%8][0] * scores[cur_state[idx%8]], unit[idx%8][1] * scores[cur_state[idx%8]]
        x2, y2 = unit[(idx+1)%8][0] * scores[cur_state[(idx+1)%8]], unit[(idx+1)%8][1] * scores[cur_state[(idx+1)%8]]
        x3, y3 = unit[(idx+2)%8][0] * scores[cur_state[(idx+2)%8]], unit[(idx+2)%8][1] * scores[cur_state[(idx+2)%8]]

        if (x2-x1) * (y3-y2) - (x3-x2) * (y2-y1) > 0: return False

    return True

def status(n):
    if n == 8:
        hexs.append([*S])
        return
    
    for idx in range(8):
        if idx not in S:
            S.append(idx)
            status(n+1)
            S.pop()

    return


def solve():
    scores = list(map(int, input().split()))

    status(0)

    ans = 0
    for cur_state in hexs:
        if isAvailable(scores, cur_state): ans += 1

    print(ans)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def refineString(words):
    res = []
    for w in words:
        if len(w) < 4:
            res.append(w)
            continue

        s = str(w[0])
        temp = []
        for ww in w[1:-1]:
            temp.append(ord(ww))
        temp.sort()
        temp = [str(x).zfill(3) for x in temp]
        
        s += str(''.join(temp))
        s += str(w[-1])

        res.append(s)

    return res


N = int(input())
W = [input().rstrip() for _ in range(N)]
M = int(input())
S = list(input().rstrip().split())

trans = {}

WX = refineString(W)
for i in range(N):
    trans[WX[i]] = W[i]

SX = refineString(S)

ans = [trans[s] for s in SX]
print(*ans)
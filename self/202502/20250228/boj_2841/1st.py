import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def fingering(n, p):
    cnt = 0

    if not S[n]:
        S[n].append(p)
        return 1

    else:
        while S[n]:
            if S[n][-1] == p:
                return cnt

            elif S[n][-1] > p:
                S[n].pop()
                cnt += 1

            else:
                break

        S[n].append(p)
        cnt += 1

    return cnt


N, P = map(int, input().split())
S = [[] for _ in range(N+1)]

ans = 0
for _ in range(N):
    n, p = map(int, input().split())
    ans += fingering(n, p)

print(ans)

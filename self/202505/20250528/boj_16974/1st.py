import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def divide_conquer(l, r, lev):
    global ans

    if l > r: return

    if l == r and l <= X:
        ans += 1
        return

    if r < X:
        ans += Ps[lev]
        return

    if l > X: return

    mid = (l+r)>>1

    if X >= mid:
        ans += 1
        divide_conquer(l+1, mid-1, lev-1)
        divide_conquer(mid+1, r-1, lev-1)
    else:
        divide_conquer(l+1, mid-1, lev-1)

    return


N, X = map(int, input().split())
Bs, Ps = [0] * (N+1), [0] * (N+1)
Ps[0] = 1

for idx in range(1, N+1):
    Bs[idx], Ps[idx] = Bs[idx-1]*2+2, Ps[idx-1]*2+1

ans = 0

divide_conquer(1, Bs[N]+Ps[N], N)

print(ans)

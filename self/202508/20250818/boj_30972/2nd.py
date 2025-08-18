import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def build_prefix(A):
    n = len(A)
    S = [[0]*n for _ in range(n)]
    for i in range(n):
        row = 0
        up = S[i-1] if i > 0 else None
        for j in range(n):
            row += A[i][j]
            S[i][j] = row + (up[j] if i > 0 else 0)
    return S

def rect_sum(S, r1, c1, r2, c2):
    # 0-based inclusive rectangle sum using prefix S
    res = S[r2][c2]
    if r1 > 0: res -= S[r1-1][c2]
    if c1 > 0: res -= S[r2][c1-1]
    if r1 > 0 and c1 > 0: res += S[r1-1][c1-1]
    return res

def weighted_sum(S, r1, c1, r2, c2):
    """
    경계: -1, 내부: +1
    ans = 전체합 - 2 * 테두리합
    (전체합은 내부+경계를 +1로 더한 값이므로, 경계만 2배 빼서 -1이 되도록 만든다)
    r1,c1,r2,c2는 0-based inclusive
    """
    total = rect_sum(S, r1, c1, r2, c2)

    # 테두리(Top/Bottom/Left/Right), 코너 중복 없이
    top    = rect_sum(S, r1, c1, r1, c2)
    bottom = rect_sum(S, r2, c1, r2, c2) if r2 > r1 else 0
    left   = rect_sum(S, r1+1, c1, r2-1, c1) if r2 - r1 + 1 > 2 else 0
    right  = rect_sum(S, r1+1, c2, r2-1, c2) if (r2 - r1 + 1 > 2 and c2 > c1) else 0

    border = top + bottom + left + right
    return total - 2 * border

def solve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = build_prefix(A)

    Q = int(input())
    out = []
    for _ in range(Q):
        r1, c1, r2, c2 = map(int, input().split())  # 1-based 입력
        # 0-based로 변환
        r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
        out.append(str(weighted_sum(S, r1, c1, r2, c2)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()

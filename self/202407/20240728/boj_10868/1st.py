import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def I(s, e, idx):
    if s == e:
        st[idx] = nums[s]
        return st[idx]

    mid = (s+e) // 2
    st[idx] = min(I(s, mid, idx*2), I(mid+1, e, idx*2+1))
    return st[idx]


def S(s, e, l, r, idx):
    if s > r or e < l:
        return float('inf')

    if s >= l and e <= r:
        return st[idx]

    mid = (s+e) // 2
    val = min(S(s, mid, l, r, idx*2), S(mid+1, e, l, r, idx*2+1))
    return val


N, M = map(int, input().split())
nums = [0]
st = [float('inf')] * (4*N)

for _ in range(N):
    nums.append(int(input()))

I(1, N, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(S(1, N, a, b, 1))

print(nums)
print(st)
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def I(s, e, tree_idx, tree, arr):
    if s == e:
        tree[tree_idx] = arr[s-1]
        return arr[s-1]
    
    mid = (s+e) >> 1
    
    tree[tree_idx] = max(I(s, mid, tree_idx*2, tree, arr), I(mid+1, e, tree_idx*2+1, tree, arr))
    
    return tree[tree_idx]


def S(s, e, l, r, tree_idx, tree):
    if s > r or e < l:
        return 0
    
    if l <= s and e <= r:
        return tree[tree_idx]
    
    mid = (s+e) >> 1
    
    return max(S(s, mid, l, r, tree_idx*2, tree), S(mid+1, e, l, r, tree_idx*2+1, tree))


def U(s, e, idx, tree_idx, val, tree):
    if s > idx or e < idx:
        return 0
    
    if s == e:
        tree[tree_idx] = val
        return val
    
    mid = (s+e) >> 1
    
    tree[tree_idx] = max(U(s, mid, idx, tree_idx*2, val, tree), U(mid+1, e, idx, tree_idx*2+1, val, tree))
    
    return tree[tree_idx]


def solve():
    N, M, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    L.sort()
    R.sort()
    
    tree = [0] * (4*N+1)
    
    I(1, N, 1, tree, arr)
    
    for _ in range(Q):
        a, b = map(int, input().split())
        
        U(1, N, a, 1, arr[b-1], tree)
        U(1, N, b, 1, arr[a-1], tree)
        
        arr[a-1], arr[b-1] = arr[b-1], arr[a-1]
        
        ans = -float("inf")
        
        for l, r in zip(L, R):
            if l > r:
                print(int(1e9))
                break
            else:
                ans = max(ans, S(1, N, l, r, 1, tree))
        else:
            print(ans)
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
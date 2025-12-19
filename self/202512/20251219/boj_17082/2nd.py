import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def I(s, e, tree_idx, tree, arr, V):
    if s == e:
        tree[tree_idx] = arr[s] if V[s] else -float("inf")
        return tree[tree_idx]
    
    mid = (s+e) >> 1
    
    tree[tree_idx] = max(I(s, mid, tree_idx*2, tree, arr, V), I(mid+1, e, tree_idx*2+1, tree, arr, V))
    
    return tree[tree_idx]


def U(s, e, idx, tree_idx, val, tree):
    if s > idx or e < idx:
        return tree[tree_idx]
    
    if s == e:
        tree[tree_idx] = val
        return val
    
    mid = (s+e) >> 1
    
    tree[tree_idx] = max(U(s, mid, idx, tree_idx*2, val, tree), U(mid+1, e, idx, tree_idx*2+1, val, tree))
    
    return tree[tree_idx]


def solve():
    N, M, Q = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    L.sort()
    R.sort()

    V = [0] * (N+1)
    cur_idx = 0
    for l, r, in zip(L, R):
        if l > r:
            for _ in range(Q): print(1_000_000_000)
            return

        l = max(cur_idx, l)
        r = max(cur_idx, r)
        
        for idx in range(l, r+1):
            V[idx] = 1
            
        cur_idx = idx
        
    tree = [0] * (4*N+1)
    
            
    I(1, N, 1, tree, arr, V)
    
    
    for _ in range(Q):
        x, y = map(int, input().split())
        
        U(1, N, x, 1, arr[y] if V[x] else -float("inf"), tree)
        U(1, N, y, 1, arr[x] if V[y] else -float("inf"), tree)
        
        arr[x], arr[y] = arr[y], arr[x]
        
        print(tree[1])


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
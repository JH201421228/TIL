import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def I(l, r, tree_idx, arr, tree, flag):
    if l == r:
        tree[tree_idx] = arr[l]
        return arr[l]
    
    mid = (l+r) >> 1
    if flag: tree[tree_idx] = max(I(l, mid, tree_idx<<1, arr, tree, flag), I(mid+1, r, tree_idx<<1|1, arr, tree, flag))
    else: tree[tree_idx] = min(I(l, mid, tree_idx<<1, arr, tree, flag), I(mid+1, r, tree_idx<<1|1, arr, tree, flag))
    
    return tree[tree_idx]


def U(l, r, idx, tree_idx, arr, tree, flag):
    if idx > r or idx < l: return
    
    if l == r:
        tree[tree_idx] = arr[idx]
        return
    
    mid = (l+r) >> 1
    U(l, mid, idx, tree_idx<<1, arr, tree, flag)
    U(mid+1, r, idx, tree_idx<<1|1, arr, tree, flag)
    
    if flag: tree[tree_idx] = max(tree[tree_idx<<1], tree[tree_idx<<1|1])
    else: tree[tree_idx] = min(tree[tree_idx<<1], tree[tree_idx<<1|1])

    return


def S(l, r, s, e, tree_idx, tree, flag):
    if s >= l and e <= r:
        return tree[tree_idx]
    
    if s > r or e < l:
        if flag: return 0
        else: return float("inf")
        
    mid = (s+e) >> 1

    if flag: return max(S(l, r, s, mid, tree_idx<<1, tree, flag), S(l, r, mid+1, e, tree_idx<<1|1, tree, flag))
    else: return min(S(l, r, s, mid, tree_idx<<1, tree, flag), S(l, r, mid+1, e, tree_idx<<1|1, tree, flag))
    

def solve():
    N, K = map(int, input().split())
    
    arr = [i for i in range(N)]
    max_tree = [0] * (4*N+1)
    min_tree = [float("inf")] * (4*N+1)
    
    I(0, N-1, 1, arr, max_tree, 1)
    I(0, N-1, 1, arr, min_tree, 0)
    
    for _ in range(K):
        Q, A, B = map(int, input().split())
        
        if Q:
            if A == S(A, B, 0, N-1, 1, min_tree, 0) and B == S(A, B, 0, N-1, 1, max_tree, 1): print("YES")
            else: print("NO")
        else:
            arr[A], arr[B] = arr[B], arr[A]
            U(0, N-1, A, 1, arr, min_tree, 0)
            U(0, N-1, B, 1, arr, min_tree, 0)
            U(0, N-1, A, 1, arr, max_tree, 1)
            U(0, N-1, B, 1, arr, max_tree, 1)
    
    return


def main():
    for _ in range(int(input())):
        solve()
    
    return


if __name__ == "__main__":
    main()
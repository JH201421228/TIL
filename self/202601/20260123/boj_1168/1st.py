import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def I(s, e, tree_idx, tree):
    if s == e:
        tree[tree_idx] = 1
        return 1
    
    mid = (s+e)>>1
    
    tree[tree_idx] = I(s, mid, tree_idx<<1, tree) + I(mid+1, e, tree_idx<<1|1, tree)
    
    return tree[tree_idx]


def U(s, e, tree_idx, target, tree):
    if s == e:
        tree[tree_idx] -= 1
        return s
    
    mid = (s+e)>>1
    
    if target <= tree[tree_idx<<1]: res = U(s, mid, tree_idx<<1, target, tree)
    else: res = U(mid+1, e, tree_idx<<1|1, target-tree[tree_idx<<1], tree)
    
    tree[tree_idx] -= 1
    
    return res
    

def solve():
    N, K = map(int, input().split())
    tree = [0] * (4*N+1)
    
    I(1, N, 1, tree)
    
    cur = K
    ans_list = []
    for t in range(N):
        ans_list.append(U(1, N, 1, cur, tree))
        
        if t == N-1: break
        cur = (cur+K-2) % (N-t-1) + 1
        
    ans = "<" + ", ".join(map(str, ans_list)) + ">"
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
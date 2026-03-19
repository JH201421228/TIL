import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MOD = 1_000_000_007


def S(s, e, l, r, tree_idx, tree):
    if s >= l and e <= r: return tree[tree_idx]
    
    if l > e or r < s: return 0
    
    mid = (s+e)>>1
    
    return S(s, mid, l, r, tree_idx<<1, tree) + S(mid+1, e, l, r, tree_idx<<1|1, tree)


def U(s, e, idx, tree_idx, tree):
    if s > idx or e < idx: return
    
    if s == e:
        tree[tree_idx] += 1
        return
    
    mid = (s+e)>>1
    
    U(s, mid, idx, tree_idx<<1, tree)
    U(mid+1, e, idx, tree_idx<<1|1, tree)
    
    tree[tree_idx] = tree[tree_idx<<1] + tree[tree_idx<<1|1]
    
    return


def solve():
    N = int(input())
    cordinate = []
    xs = []
    for _ in range(N):
        x, y = map(int, input().split())
        cordinate.append((x, y))
        xs.append(x)
        
    xs.sort()
    
    x_dict = {}
    cur = 1
    for x in xs:
        if x not in x_dict:
            x_dict[x] = cur
            cur += 1
        
    cordinate.sort(key=lambda x: x[1])
    
    M = len(x_dict)
    tree = [0] * (4*M+1)
    
    ans = 0
    
    while cordinate:
        cur_x, cur_y = cordinate.pop()
        candidate = [cur_x]
        
        while cordinate and cordinate[-1][-1] == cur_y:
            cur_x, cur_y = cordinate.pop()
            candidate.append(cur_x)
        
        for x in candidate:
            ans += S(1, M, 1, x_dict[x]-1, 1, tree) * S(1, M, x_dict[x]+1, M, 1, tree)
            ans %= MOD
            
        for x in candidate:
            U(1, M, x_dict[x], 1, tree)
            
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
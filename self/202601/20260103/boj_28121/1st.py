import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(idx, parent):
    root = idx
    
    while root != parent[root]: root = parent[root]

    while root != idx:
        p = parent[idx]
        parent[idx] = root
        idx = p
    
    return root


def union(a, b, parent, sets, odd, is_ans, ans):
    pa, pb = find(a, parent), find(b, parent)
    
    if is_ans[pa] or is_ans[pb]:
        if not is_ans[pa]:
            ans += len(sets[pa])
            is_ans[pa] = 1
        if not is_ans[pb]:
            ans += len(sets[pb])
            is_ans[pb] = 1
    
    if len(sets[pa]) < len(sets[pb]):
        sets[pa], sets[pb] = sets[pb], sets[pa]
        
    parent[pb] = pa
        
    if odd[a] == odd[b]:
        for v in sets[pb]:
            sets[pa].add(v)
            odd[v] = 1 - odd[v]
        sets[pb].clear()
    else:
        sets[pa].update(sets[pb])
        sets[pb].clear()
    
    return ans


def solve():
    N, Q = map(int, input().split())

    parent = [i for i in range(N+1)]
    odd = [0] * (N+1)
    sets = [set([i]) for i in range(N+1)]
    is_ans = [0] * (N+1)
    
    ans = 0
    
    output = ""
    
    for _ in range(Q):
        a, b = map(int, input().split())
        
        pa, pb = find(a, parent), find(b, parent)
        
        if pa == pb and odd[a] == odd[b] and not is_ans[pa]:
            is_ans[pa] = 1
            ans += len(sets[pa])
        
        if pa != pb:
            ans = union(a, b, parent, sets, odd, is_ans, ans)
            
        output += str(ans) + '\n'
        
    print(output)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
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


def union(a, b, parent, state, debt, sets):
    pa, pb = find(a, parent), find(b, parent)
        
    if len(sets[pa]) < len(sets[pb]):
        pa, pb = pb, pa
        
    parent[pb] = pa
    
    cost = (debt[pa] // len(sets[pa])) - (debt[pb] // len(sets[pb]))
    debt[pa] = (debt[pa] // len(sets[pa])) * (len(sets[pa]) + len(sets[pb]))
    
    for v in sets[pb]:
        sets[pa].add(v)
        state[v] += cost
        
    sets[pb].clear()
    
    return


def solve():
    N, M = map(int, input().split())
    
    parent = [i for i in range(N+1)]
    state = [0] * (N+1)
    debt = [0] * (N+1)
    sets = [set([i]) for i in range(N+1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        
        if a == 1:
            union(b, c, parent, state, debt, sets)
        else:
            p = find(b, parent)
            debt[p] += c
            state[b] += c
            
    p = find(1, parent)
    
    if debt[p]:
        cost = debt[p] // N
        
        for idx in range(1, N+1):
            state[idx] -= cost
    
    ans = ""
    cnt = 0
    
    for idx in range(1, N+1):
        if idx == p or not state[idx]: continue
        
        cnt += 1
        
        if state[idx] > 0: ans += f"{p} {idx} {state[idx]}\n"
        else: ans += f"{idx} {p} {-state[idx]}\n"
    
    print(cnt)
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
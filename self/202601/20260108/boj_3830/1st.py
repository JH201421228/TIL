import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(idx, arr):
    root = idx
    
    while (root != arr[root]): root = arr[root]
    
    while (idx != root):
        p = arr[idx]
        arr[idx] = root
        idx = p
         
    return root


def union(a, b, w, arr, sets, state):
    pa = find(a, arr)
    pb = find(b, arr)
    
    fix = state[a] - state[b]
    
    if len(sets[pa]) < len(sets[pb]):
        sets[pa], sets[pb] = sets[pb], sets[pa]
        w *= -1
        fix *= -1
        
    arr[pb] = pa
    
    for v in sets[pb]:
        sets[pa].add(v)
        state[v] += w+fix

    return


def solve(N, M):
    arr = [i for i in range(N+1)]
    state = [0] * (N+1)
    sets = [set([i]) for i in range(N+1)]
    
    for _ in range(M):
        temp = list(input().rstrip().split())
        
        pa, pb = find(int(temp[1]), arr), find(int(temp[2]), arr)
        
        if temp[0] == "!":
            
            if pa != pb:
                union(int(temp[1]), int(temp[2]), int(temp[3]), arr, sets, state)
                
        else:
            if pa != pb: print("UNKNOWN")
            else: print(state[int(temp[2])] - state[int(temp[1])])
    
    return


def main():
    while True:
        N, M = map(int, input().split())
        if not N and not M: break
        
        solve(N, M)
    
    return


if __name__ == "__main__":
    main()
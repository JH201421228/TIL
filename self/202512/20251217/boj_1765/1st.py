import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def find(n, arr):
    if arr[n] == n: return n
    
    arr[n] = find(arr[n], arr)
    
    return arr[n]


def union(a, b, arr):
    a, b = find(a, arr), find(b, arr)
    
    arr[max(a, b)] = min(a, b)
    
    return


def set_update(a, b, arr, arr_set):
    if len(arr_set[a]) < len(arr_set[b]):
        arr_set[a], arr_set[b] = arr_set[b], arr_set[a]
        
    arr_set[a].update(arr_set[b])
    arr_set[b].clear()
    
    union(a, b, arr)
    
    return



def solve():
    N = int(input())
    M = int(input())
    
    arr = [i for i in range(N+1)]
    arr_set = [set([i]) for i in range(N+1)]
    enemies = [set() for _ in range(N+1)]
    
    for _ in range(M):
        temp = tuple(input().rstrip().split())
        
        if temp[0] == "F":
            a, b = find(int(temp[1]), arr), find(int(temp[2]), arr)
            
            if a == b: continue
            
            set_update(a, b, arr, arr_set)
        
        else:
            a, b = int(temp[1]), int(temp[2])
            
            for e in enemies[a]:
                x, y = find(e, arr), find(b, arr)
                
                if x == y: continue
                
                set_update(x, y, arr, arr_set)
                
            for e in enemies[b]:
                x, y = find(e, arr), find(a, arr)
                
                if x == y: continue
                
                set_update(x, y, arr, arr_set)
                
            enemies[a].add(b)
            enemies[b].add(a)
        
    ans = 0
    
    for s in arr_set[1:]:
        if s: ans += 1
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(n, arr):
    if n == arr[n]:
        return n
    
    arr[n] = find(arr[n], arr)
    
    return arr[n]
    

def union(n, m, arr):
    arr[find(m, arr)] = find(n, arr)
    
    return


def solve():
    G = int(input())
    P = int(input())
    
    history = [i for i in range(G+1)]
    
    ans = 0
    
    for _ in range(P):
        cur = int(input())
        
        res = find(cur, history)
        
        if not res:
            break
    
        union(res-1, res, history)
    
        ans += 1
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def B(n, C, V, G):
    for x in G[n]:
        if V[x]: continue
        
        V[x] = 1
        if not C[x] or B(C[x], C, V, G):
            C[x] = n
            
            return True
    
    return False


def solve():
    K, N = map(int, input().split())
    
    G = [[] for _ in range(N+1)]
    
    chicken = [int(input()) for _ in range(K)]
    
    for n in range(1, N+1):
        a, b = map(int, input().split())
        
        for c in range(K):
            tmp = chicken[c]
            if tmp >= a and tmp <= b:
                G[n].append(c+1)
                
    C = [0] * (K+1)
    
    ans = 0
    
    for n in range(1, N+1):
        V = [0] * (K+1)
        if B(n, C, V, G): ans += 1
        
    print(ans)
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
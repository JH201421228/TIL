import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    P = [0] * N
    
    for _ in range(N-1):
        u, v = map(int, input().split())
        P[v] = u
    
    state = list(map(int, input().split()))
    
    ans = 0
    for i in range(1<<N):
        temp = []
        for j in range(N):
            if i & (1<<j): temp.append(j)
            
        V = [0] * N
        for t in temp:
            V[t] = 1
        
        if not V[0]: continue
        
        is_available = True
        
        for t in temp:
            if not is_available: break
            
            while True:
                t = P[t]
                if t == 0: break
                
                if not V[t]:
                    is_available = False
                    break
        
        
        if is_available:
            tmp, cnt = 0, 0
            for t in temp:
                if state[t] == 1: cnt += 1
                elif state[t] == 2: tmp += 1
        
        if cnt <= K: ans = max(ans, tmp)
    
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(x, y, P, D):
    if x == y: return [x]
    
    X, Y = [x], [y]
    
    d_x, d_y = D[x], D[y]
    
    if d_x > d_y:
        while d_x > d_y:
            x = P[x]
            X.append(x)
            d_x -= 1
    else:
        while d_y > d_x:
            y = P[y]
            Y.append(y)
            d_y -= 1
    
    if x == y:
        Y.reverse()
        X.pop()
        return X+Y
    
    while True:
        x, y = P[x], P[y]
        X.append(x)
        if x == y: break
        Y.append(y)
        
    Y.reverse()
    
    return X+Y


def set_depth(N, P):
    V = [-1] * (N+1)
    V[1] = 1
    
    for i in range(1, N+1):
        if V[i] != -1: continue
        
        d = i
        
        depth = 0
        while V[d] == -1:
            d = P[d]
            depth += 1
        
        depth += V[d]
        
        d = i
        while V[d] == -1:
            V[d] = depth
            depth -= 1
        
    return V


def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    P = [i for i in range(N+1)]
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        P[max(a, b)] = min(a, b)
        
    
    D = set_depth(N, P)
    
    ans = []
    
    for _ in range(Q):
        x, y = map(int, input().split())
        ans.append(find(y, x, P, D))
    
    string = ""
    MOD = 1_000_000_007
    
    for a in ans:
        tmp = 0
        l = 0
        
        for s in a:
            tmp = (tmp + (A[s-1] * pow(10, l, MOD)) % MOD) % MOD
            l += len(str(A[s-1]))

        string += str(tmp)
        string += "\n"
        
    print(string)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
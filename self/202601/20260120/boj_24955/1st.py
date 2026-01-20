import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(x, y, P, V):
    ans = [x]
    cnt = 1
    V[x] = cnt
    cnt += 1
    
    while x != 1:
        x = P[x]
        ans.append(x)
        V[x] = cnt
        cnt += 1
        
        if x == y: break
        
    if x != 1: return ans
    
    temp = [y]
    
    while y != 1:
        y = P[y]
        
        if V[y]: break
        
        temp.append(y)
        
    temp.reverse()
        
    ans = ans[:V[y]-1] + temp
    
    return ans


def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    P = [i for i in range(N+1)]
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        P[max(a, b)] = min(a, b)
    
    ans = []
    
    for _ in range(Q):
        V = [0] * (N+1)
        x, y = map(int, input().split())
        temp = find(max(x, y), min(x, y), P, V)
        if x > y: temp.reverse()
        
        ans.append(temp)
        
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
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    A, B = [], []
    
    for _ in range(N):
        a, b = map(int, input().split())
        
        if a < b:
            A.append((a, b))
        else:
            B.append((a, b))
            
    A.sort()
    B.sort(key=lambda x : x[1], reverse=True)
    
    ans, rest = 0, 0
    
    for a, b in A + B:
        if rest < a:
            ans += (a-rest)
            rest = a
            
        rest += (b-a)
        
    print(ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
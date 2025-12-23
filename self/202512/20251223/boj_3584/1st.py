import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    parent = [i for i in range(N+1)]
    V = [0] * (N+1)
    
    for _ in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a
        
    a, b = map(int, input().split())
    
    while True:
        V[a] = 1
        
        if parent[a] == a:
            break
        
        a = parent[a]
        
    while True:
        if V[b]:
            print(b)
            break
        
        b = parent[b]
    
    return


def main():
    for _ in range(int(input())):
        solve()
    
    return


if __name__ == "__main__":
    main()
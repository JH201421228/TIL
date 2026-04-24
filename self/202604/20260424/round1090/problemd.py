import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    ans = [1, 2, 6]
    
    if N <= 3:
        print(*ans[:N])
        return
    
    for i in range(2, N-1):
        ans.append((2*i-1) * (2*i+1))
        
    print(*ans)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()
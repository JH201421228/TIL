import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    arr = [0] * N
    
    for i in range(N):
        idx = N//2 + ((-1)**i) * ((i+1)//2)
        arr[idx] = N-i
        
    print(*arr)
    
    return


def main():
    solve()
    return


if __name__ == "__main__":
    main()
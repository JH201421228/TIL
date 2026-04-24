import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    ans = []
    s, e = 1, 3*N
    for cur in range(3*N):
        if cur%3:
            ans.append(e)
            e -= 1
        else:
            ans.append(s)
            s += 1
            
    print(*ans)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()
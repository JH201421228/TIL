import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    N //= 2
    P = N**2
    
    x, y = 0, N-1
    cnt = 0
    delta = [(1, 0), (0, -1), (1, -1)]
    
    while x != y:
        for dx, dy in delta:
            xx, yy = x+dx, y+dy
            if xx**2 + yy**2 < P and (xx+1)**2 + (yy+1)**2 > P:
                cnt += 1
                x, y = xx, yy
                break
    
    print(cnt*8 + 4)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def ccw(a, b, c, d):
    return a*d - b*c


def solve():
    points = [tuple(map(int, input().split()))for _ in range(3)]
    
    res = ccw(points[1][0] - points[0][0], points[1][1] - points[0][1], points[2][0] - points[0][0], points[2][1] - points[0][1])
    
    if res > 0: print(1)
    elif res < 0: print(-1)
    else: print(0)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
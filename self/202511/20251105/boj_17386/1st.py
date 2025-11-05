import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def cross_product(p1, p2, p3):
    return (p3[0] - p2[0]) * (p2[1] - p1[1]) - (p3[1] - p2[1]) * (p2[0] - p1[0])


def solve():
    lines = [tuple(map(int, input().split())) for _ in range(2)]
    
    if cross_product(lines[0][:2], lines[0][2:], lines[1][:2]) * cross_product(lines[0][:2], lines[0][2:], lines[1][2:]) < 0 and cross_product(lines[1][:2], lines[1][2:], lines[0][:2]) * cross_product(lines[1][:2], lines[1][2:], lines[0][2:]) < 0:
        print(1)
    else:
        print(0)
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
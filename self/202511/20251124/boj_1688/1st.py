import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def ccw(p1, p2, p3):    
    return (p3[0] - p1[0]) * (p2[1] - p3[1]) - (p3[1] - p1[1]) * (p2[0] - p3[0])


def is_cross_line(N, dots, p3):
    
    res = 0
    
    for idx in range(N):
        p1 = dots[idx]
        p2 = dots[(idx+1) % N]
        
        if p1[1] < p2[1]:
            p1, p2 = p2, p1
            
        if ccw(p1, p2, p3) == 0:
            if p3[0] >= min(p1[0], p2[0]) and p3[0] <= max(p1[0], p2[0]) and p3[1] >= min(p1[1], p2[1]) and p3[1] <= max(p1[1], p2[1]):
                return True
            
        if p3[0] > max(p1[0], p2[0]): continue
        
        if p3[1] >= max(p1[1], p2[1]): continue
        
        if p3[1] < min(p1[1], p2[1]): continue
        
        if ccw(p1, p2, p3) > 0: res += 1
    
    
    return res%2


def solve():
    N = int(input())
    dots = [tuple(map(int, input().split())) for _ in range(N)]
    
    for idx in range(3):
        if is_cross_line(N, dots, tuple(map(int, input().split()))):
            print(1)
        else:
            print(0)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
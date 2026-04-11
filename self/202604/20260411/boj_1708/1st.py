import sys
import math
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N = int(input())
    
    dots = [tuple(map(int, input().split())) for _ in range(N)]

    dots.sort(key=lambda x: (x[1], x[0]))
    
    origin = dots[0]
    
    dots = dots[1:]
    
    dots.sort(key=lambda x: (math.atan2(x[1] - origin[1], x[0] - origin[0]), (x[1] - origin[1])**2 + (x[0] - origin[0])**2))
    
    q = [origin]
    
    for dot in dots:
        if len(q) < 2: q.append(dot)
        else:
            while len(q) >= 2:
                dx1, dy1 = q[-1][0] - q[-2][0], q[-1][1] - q[-2][1]
                dx2, dy2 = dot[0] - q[-1][0], dot[1] - q[-1][1]
                if dx1 * dy2 - dy1 * dx2 > 0: break
                q.pop()
                
            q.append(dot)
            
    print(len(q))
    

def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
    
import sys
import math
sys.stdin = open("input.txt")
input = sys.stdin.readline


def ccw(d1, d2, d3):
    return (d2[0] - d1[0]) * (d3[1] - d1[1]) - (d2[1] - d1[1]) * (d3[0] - d1[0])


def solve():
    temp = list(map(int, input().split()))
    dots = []
    
    for i in range(temp[0]):
        dots.append((temp[2*i+1], temp[2*i+2], i))
    
    dots.sort(key=lambda x: (x[1], x[0]))
    
    origin = dots[0]
    dots = dots[1:]
    
    dots.sort(key=lambda x: (
        math.atan2(x[1] - origin[1], x[0] - origin[0]),
        (x[0] - origin[0])**2 + (x[1] - origin[1])**2
    ))
    
    idx = temp[0]-2
    while idx > 0 and ccw(origin, dots[idx], dots[idx-1]) == 0: idx -= 1
    
    dots[idx:] = reversed(dots[idx:])
    
    ans = f"{origin[2]}"
    
    for _, _, target in dots: ans += f" {target}"
    
    print(ans)
    
    return


def main():
    for _ in range(int(input())): solve()
    
    return


if __name__ == "__main__":
    main()
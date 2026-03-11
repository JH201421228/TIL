import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
# 25_000_000

def solve():
    N = int(input())
    locations = []
    
    for _ in range(N):
        locations.append(tuple(map(int, input().split())))
        
    res = 0
    
    for i in range(N-1):
        for j in range(i+1, N):
            res += ((locations[i][0]-locations[j][0])**2 + (locations[i][1]-locations[j][1])**2)**.5

    print(res*2 / N)
        
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
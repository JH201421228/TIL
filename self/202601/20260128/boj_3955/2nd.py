import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MAX = 1_000_000_000


def xgcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = xgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def solve():
    K, C = map(int, input().split())
    
    g, y, x = xgcd(K, C)
    
    if g != 1:
        print("IMPOSSIBLE")
        return
    
    y = (y%K + K) % K
    
    if not y: y += K
    
    if y > MAX: print("IMPOSSIBLE")
    else: print(y)
    
    return


def main():
    for _ in range(int(input())):
        solve()
    
    return


if __name__ == "__main__":
    main()
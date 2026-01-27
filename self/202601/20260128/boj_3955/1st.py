import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


MAX = 1_000_000_000

def egcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def solve_one():
    K, C = map(int, input().split())
    
    if C == 1:
        y = K + 1
        return y if y <= MAX else "IMPOSSIBLE"
    
    if K == 1:
        return 1

    g, x, y = egcd(C, K)
    if g != 1:
        return "IMPOSSIBLE"

    Y = x % K
    if Y == 0:
        Y += K

    if Y > MAX:
        return "IMPOSSIBLE"
    
    return Y


def main():
    for _ in range(int(input())):
        print(solve_one())
    
    return


if __name__ == "__main__":
    main()
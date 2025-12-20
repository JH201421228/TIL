import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def inv(a, b):
    res = 1
    for _ in range(b-2):
        res *= a
        res %= b
        
    return res
        


def solve():
    m, seed, x1, x2 = map(int, input().split())
    
    a = (x1 - x2) % m * pow((seed-x1) % m, m-2, m) % m
    c = (x1 - a * seed) % m
    
    print(a, c)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
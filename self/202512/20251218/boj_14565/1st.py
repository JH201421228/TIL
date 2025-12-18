import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a%b
        
    return a


def recur(a, b):
    if a == 1:
        x = 1+b
        y = 1
        return x, y
    elif b == 1:
        x = 1
        y = a-1
        return x, y
    else:
        if a > b:
            x, y = recur(a%b, b)
            y = (a*x - 1) // b
            return x, y
        else:
            x, y = recur(a, b%a)
            x = (b*y + 1) // a
            return x, y
            

def inverse(n, a):
    if gcd(n, a) == 1:
        x, y = recur(a, n)
        return x%n
    else: return -1


def solve():
    N, A = map(int, input().split())
    
    print(N-A, inverse(N, A))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
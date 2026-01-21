import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def gcd(a, b):
    if not b: return 0, 0
    x, y = a, b
    
    while y:
        x, y = y, x%y
        
    return a//x, b//x


def out(a, b, c):
    space = len(str(a)) + 1
    ans = ' ' * space + str(c) + '\n' + str(a) + ' ' + '-'*len(str(b)) + '\n' + ' ' * space + str(b)
    print(ans)
    
    return
    

def solve(n):
    if n == 1:
        print(1)
        return
    
    denominate = 1
    for i in range(2, n): denominate *= i
    
    numerator = 0
    for i in range(2, n): numerator += n * (denominate // i)
    
    a, b, c = numerator//denominate + n+1, *gcd(denominate, numerator%denominate)
    
    if not b: print(a)
    else:
        out(a, b, c)
    
    return


def main():
    while True:
        try:
            solve(int(input()))
        except: break
    
    return


if __name__ == "__main__":
    main()
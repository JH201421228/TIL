import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


for _ in range(int(input())):
    n, m, num = 0, 0, []
    q = deque(list(input().rstrip()))
    q.popleft()
    q.popleft()

    isN = True
    while q:
        o = q.popleft()
        if o == ')':
            break
        elif o == '(':
            isN = not isN
        else:
            num.append(o)
            if isN:
                n += 1
            else:
                m += 1

    u, d = 0, 0
    if not m:
        u = int(''.join(num[:]))
        d = 10 ** n
        g = gcd(d, u)
        print(''.join([str(u // g), '/', str(d // g)]))
    else:
        u = int(''.join(num[:])) - int(''.join(num[:n])) if n > 0 else int(''.join(num[:]))
        d = (10 ** (n+m)) - (10 ** n)
        g = gcd(d, u)
        print(''.join([str(u // g), '/', str(d //g)]))
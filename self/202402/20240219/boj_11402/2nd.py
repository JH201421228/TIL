import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, k, mo = map(int, input().split())



def fatorial(a):
    ans = 1
    for i in range(2, a+1):
        ans = (ans * i) % mo
    return ans


def div_con(m, p):
    if p == 0:
        return 1
    if p == 1:
        return m

    num = div_con(m, p//2)
    if p%2:
        return num**2 * m % mo
    else:
        return  num**2 % mo

top = fatorial(n) % mo
bottom = div_con(fatorial(k) * fatorial(n-k) % mo, mo - 2)
print(top * bottom % mo)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n, k, mo = map(int, input().split())


def fatorial(a):
    ans = 1
    for i in range(2, a+1):
        ans = (ans * i) % mo if (ans * i) % mo else 1
    return ans


def div_con(m, p):
    if p == 0:
        return 1
    if p == 1:
        return m

    num = div_con(m, p//2)
    if p % 2:
        return num**2 * m % mo if num**2 * m % mo else 1
    else:
        return num**2 % mo if num**2 % mo else 1

top = fatorial(n) % mo
# top = top if top else 1
bot1 = fatorial(k) % mo
bot1 = bot1 if bot1 else 1
bot2 = fatorial(n-k) % mo
bot2 = bot2 if bot2 else 1
bot = bot1 * bot2 % mo if bot1 * bot2 % mo else 1
bottom = div_con(bot, mo - 2)
print(top * bottom % mo)
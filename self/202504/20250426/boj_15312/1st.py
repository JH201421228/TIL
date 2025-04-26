import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a,b):
    while b:
        a, b = b, a%b

    return a


N, M = map(int, input().split())
ratios = [tuple(map(int, input().split())) for _ in range(N)]
ratios.sort(key=lambda x:-x[1]/x[0])

idx = 0
sugar, water = 0, 0

while water < M:
    if water + ratios[idx][0] < M:
        sugar += ratios[idx][1]
        water += ratios[idx][0]
        idx += 1
    else:
        mod = gcd(max((M-water)*ratios[idx][1], ratios[idx][0]), min((M-water)*ratios[idx][1], ratios[idx][0]))
        top, bot = ((M-water)*ratios[idx][1])//mod, ratios[idx][0]//mod
        print(top+bot*sugar, '/', bot, sep='')
        exit(0)
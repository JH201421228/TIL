import sys
sys.stdin = open('inpu.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    corridor = [0] * 200
    for __ in range(int(input())):
        s, e = map(int, input().split())
        s, e = min(s, e), max(s, e)
        for idx in range((s-1)//2, (e-1)//2+1):
            corridor[idx] += 1

    print(max(corridor) * 10)
import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    N, M, X = map(int, input().split())
    graph =
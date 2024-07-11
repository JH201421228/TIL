import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


H, W = map(int, input().split())
R = []
for _ in range(H):
    R.append(list(map(int, input().split())))

G = [[] for _ in range(H*W+1)]
for i in range(H):
    for j in range(W):
        if
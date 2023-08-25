import sys
sys.stdin = open('input.txt')

N = int(input())
tree = [0] * (N+1)
for _ in range(N-1):
    parents, child = map(int, input().split())
    tree[child] = parents

for i in range(2, N+1):
    print(tree[i])
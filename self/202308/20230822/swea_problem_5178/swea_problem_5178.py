import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M, L = map(int, input().split())
    leaf = [list(map(int, input().split())) for _ in range(M)]
    tree = [0] * (N + 1)
    for idx, val in leaf:
        tree[idx] = val
    for i in range(N, 0, -1):
        child = i
        parent = child // 2
        if parent:
            tree[parent] += tree[child]

    print(f'#{test+1} {tree[L]}')
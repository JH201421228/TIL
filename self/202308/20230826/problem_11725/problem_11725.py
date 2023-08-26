import sys
sys.stdin = open('input.txt')

n = int(input())
tree_info = [[] for _ in range(n+1)]
for _ in range(n-1):
    p1, p2 = map(int, input().split())
    tree_info[p1].append(p2)
    tree_info[p2].append(p1)
# print(tree_info)

checker = [0] * (n+1)
checker[1] = 1
que = [1]
while que:
    now = que.pop(0)
    for val in tree_info[now]:
        if not checker[val]:
            checker[val] = now
            que.append(val)
for idx in range(2, n+1):
    print(checker[idx])
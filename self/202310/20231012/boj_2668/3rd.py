import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(n):
    if not visited[n]:
        visited[n] = 1
        temp1.add(n)
        temp2.add(input_list[n])
        if temp1 == temp2:
            ans.extend(list(temp1))
            return
        dfs(input_list[n])
    visited[n] = 0


ans = []
N = int(input())
input_list = [0]
for _ in range(N):
    input_list.append(int(input()))

for idx in range(1, N+1):
    visited = [0] * (N+1)
    temp1 = set()
    temp2 = set()
    dfs(idx)
ans = sorted(list(set(ans)))
print(len(ans))
for num in ans:
    print(num)

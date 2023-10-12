import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 입력받은 리스트의 idx + 1 값들의 집합이, 해당 idx의 집합들과 일치하면 됨
# 상기 조건 하에서 가장 많은 집합 요소의 개수를 정답으로 인정
# 자기 인덱스에서 여행을 떠나서 본인 인덱스로 돌아올 수 있으면 해당 숫자들은 모두 집합으로 묶을 수 있음.


def dfs(start, val, temp):
    if val in temp:
        return
    temp.append(val)
    if start == val:
        for num in temp:
            visited[num] = 1
        return
    dfs(start, input_list[val], temp)



input_list = [0]
N = int(input())
for _ in range(N):
    input_list.append(int(input()))

visited = [0] * (N+1)
ans_list = []
for idx in range(1, N+1):
    if not visited[idx]:
        temp = []
        dfs(idx, input_list[idx], temp)
        ans_list.extend(temp)
print(sorted(list(set(ans_list))))
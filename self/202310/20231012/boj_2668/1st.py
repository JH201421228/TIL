import sys
sys.stdin = open('input.txt')

# 입력받은 리스트의 idx + 1 값들의 집합이, 해당 idx의 집합들과 일치하면 됨
# 상기 조건 하에서 가장 많은 집합 요소의 개수를 정답으로 인정
# 자기 인덱스에서 여행을 떠나서 본인 인덱스로 돌아올 수 있으면 해당 숫자들은 모두 집합으로 묶을 수 있음.


def dua_lipa(start):
    stack = [start]
    return_list = []
    check_list = [0] * (N+1)
    check_list[start] = 1
    while stack:
        idx = stack.pop()
        next_idx = input_list[idx]
        if not check_list[next_idx]:
            check_list[next_idx] = 1
            stack.append(next_idx)
            return_list.append(next_idx)
            if next_idx == start:
                for num in return_list:
                    visited[num] = 1
                return return_list
    return False

input_list = [0]
N = int(input())
for _ in range(N):
    input_list.append(int(input()))
print(input_list)
visited = [0] * (N+1)
ans_list = []
for idx in range(1, N+1):
    if not visited[idx]:
        temp = dua_lipa(idx)
        if temp:
            ans_list.extend(temp)
print(ans_list)


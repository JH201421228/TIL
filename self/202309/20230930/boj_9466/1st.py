import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

def holiday(start, next, temp):
    if temp and start == next:
        global ans
        ans += len(temp)
        for idx in temp:
            ans_visited[idx] = 1
        return
    if not visited[stu_list[next] - 1]:
        visited[stu_list[next] - 1] = 1
        temp.append(stu_list[next] - 1)
        holiday(start, stu_list[next] - 1, temp)
        visited[stu_list[next] - 1] = 0



for _ in range(int(input())):
    N = int(input())
    stu_list = list(map(int, input().split()))
    ans_visited = [0] * N
    ans = 0
    for idx in range(N):
        if not ans_visited[idx]:
            visited = [0] * N
            temp_list = []
            holiday(idx, idx, temp_list)
    # print(ans_visited)
    print(N - ans)
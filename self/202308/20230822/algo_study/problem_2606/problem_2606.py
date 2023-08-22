import sys
from collections import deque
sys.stdin = open('input.txt')


def computer_virus_num(num, start):
    stack = [start] # 탐색지점을 저장할 큐를 선언합니다.
    trace = [0] * (num+1) # 탐색 유무를 기록할 리스트를 선언합니다.
    trace[start] = 1 # 탐색을 시작하는 컴퓨터에 탐색했음을 기록합니다.

    while stack: # 큐에 값이 있는동안 반복합니다.
        now = stack.pop() # 현재 탐색할 컴퓨터를 변수에 저장합니다.
        for next in graph[now]: # 컴퓨터간 연결정보를 참고하여 다음 탐색할 지점을 선정합니다.
            if not trace[next]: # 다음 탐색지점으로 선정된 곳의 탐색 유무를 검사합니다.
                trace[next] = 1 # 아직 탐색하지 않은 곳이라면 탐색 유무를 기록합니다.
                stack.append(next) # 탐색한 지점을 큐에 저장합니다.
    return sum(trace) - 1 # 탐색 가능한 컴퓨터중 감염이 시작된 컴퓨터를 제외한 값을 반환합니다.


computer_num = int(input()) # 컴퓨터의 개수를 받아옵니다.
E = int(input()) # 간선의 개수를 받아옵니다.
graph = [[] for _ in range(computer_num + 1)] # 컴퓨터간의 연결 정보를 저장할 리스트를 선언합니다.
for _ in range(E): # 컴퓨터간의 연결 정보를 받아옵니다.
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
print(computer_virus_num(computer_num, 1))

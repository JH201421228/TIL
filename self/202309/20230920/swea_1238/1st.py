import sys
from collections import deque
sys.stdin = open('input.txt')


def maroon_5_this_love():
    temp = []
    while que:
        now, cnt = que.popleft()
        for next in graph[now]:
            if not check_list[next]:
                check_list[next] = 1
                que.append([next, cnt + 1])
                temp.append([cnt + 1, next])
    temp.sort()
    return temp[-1][-1]



for test in range(10):
    data_len, start = map(int, input().split())
    nums_list = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    check_list = [0] * 101
    que = deque([[start, 0]])
    for idx in range(data_len//2):
        graph[nums_list[idx * 2]].append(nums_list[idx * 2 + 1])
    # print(graph)
    # for node in range(1, 101):
    #     if not check_list[node]:
    #         maroon_5_this_love(node)
    print(f'#{test + 1} {maroon_5_this_love()}')

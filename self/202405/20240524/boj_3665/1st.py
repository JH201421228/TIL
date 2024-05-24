import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())

    order_dict = {}
    order_graph = [[0] * (N+1) for _ in range(N+1)]

    temp = list(map(int, input().split()))

    order_dict[temp[0]] = 0

    for idx in range(N-1):
        for jdx in range(idx+1, N):
            order_graph[temp[idx]][temp[jdx]] = 1
            order_dict[temp[jdx]] = order_dict.get(temp[jdx], 0) + 1

    for _ in range(int(input())):
        s, e = map(int, input().split())
        if order_graph[s][e]:
            order_graph[s][e] = 0
            order_graph[e][s] = 1
            order_dict[e] -= 1
            order_dict[s] = order_dict.get(s, 0) + 1
        else:
            order_graph[s][e] = 1
            order_graph[e][s] = 0
            order_dict[e] = order_dict.get(e, 0) + 1
            order_dict[s] -= 1

    # print(order_dict)

    ans = [False] * N
    isPossible = True
    for key, value in order_dict.items():
        if ans[value] == False:
            ans[value] = key
        else:
            isPossible = False
            break

    if isPossible:
        print(*ans)
    else:
        print('IMPOSSIBLE')
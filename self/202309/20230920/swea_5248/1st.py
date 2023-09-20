import sys
sys.stdin = open('input.txt')


def i_need_friend(num):
    check_list[num] = 1

    for next in graph[num]:
        if not check_list[next]:
            check_list[next] = 1
            i_need_friend(next)


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    nums_list = list(map(int, input().split()))
    # 짝수 노드에서 바로 다음 홀수 노드로 연결됨
    graph = [[] for _ in range(N+1)]
    # print(graph)
    # print(nums_list)
    for idx in range(M):
        graph[nums_list[idx * 2]].append(nums_list[idx * 2 + 1])
        graph[nums_list[idx * 2 + 1]].append(nums_list[idx * 2])
    # print(graph)
    check_list = [0] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if not check_list[i]:
            i_need_friend(i)
            ans += 1
    print(f'#{test + 1} {ans}')

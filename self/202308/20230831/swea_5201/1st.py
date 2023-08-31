import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    N, M = map(int, input().split()) # N: container, M: truck
    freight_container = list(map(int, input().split()))
    freight_truck = list(map(int, input().split()))
    freight_truck.sort()

    ans_list = []
    while freight_truck:
        now_truck = freight_truck.pop()
        now_container = 0
        now_container_idx = False
        for idx in range(N):
            if freight_container[idx] > now_container and freight_container[idx] <= now_truck:
                now_container = freight_container[idx]
                now_container_idx = idx
        if not now_container:
            break
        else:
            ans_list.append(now_container)
            freight_container[now_container_idx] = 51
    # print(ans_list)
    print(f'#{test+1} {sum(ans_list)}')
import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    container_num, truck_num = map(int, input().split())
    freight_container = list(map(int, input().split()))
    freight_truck = list(map(int, input().split()))
    freight_truck.sort()
    ans_list = []
    # print(freight_container[0])
    while freight_truck:
        now_truck = freight_truck.pop()
        now_container = 0
        now_idx = -1
        for idx in range(container_num):
            if freight_container[idx] > now_container and freight_container[idx] <= now_truck:
                now_container = freight_container[idx]
                now_idx = idx
        if now_idx == -1:
            break
        else:
            ans_list.append(now_container)
            freight_container[now_idx] = 51
    print(f'#{test+1} {sum(ans_list)}')


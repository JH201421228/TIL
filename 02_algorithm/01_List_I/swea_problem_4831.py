T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    bus_list = list(map(int, input().split()))
    ans = 0

    bus_list.insert(0, 0)
    bus_list.append(N)
    # 버스 정류장에 시작구간 및 끝 구간 추가
    # [0, 1, 3, 5, 7, 9, 10]

    for_ans_list = []

    for j in range(len(bus_list)-1):
        if bus_list[j+1] - bus_list[j] > K:
            ans = -1
            break
        else:
            for_ans_list.append(bus_list[j+1] - bus_list[j])
    # 구간 사이 거리가 K보다 크면 전기버스는 갈 수 없음. break후 ans = -1을 반환
    # 구간 사이 거리가 모두 K보다 작을시 정류장 사이 거리를 for_ans_list에 추가
    # [1, 2, 2, 2, 2, 1]

    for_ans_list.append(0)
    # 하기 j+1 인덱스까지 참조할 예정이므로 마지막에 0을 추가

    if ans != -1:
        j = 0
        while True:

            if for_ans_list[j+1] + for_ans_list[j] <= K:
                for_ans_list[j] = (for_ans_list[j+1] + for_ans_list[j])
                del for_ans_list[j+1]
            # 인접한 구간 사이 거리가 K보다 작거나 같을때 인접한 값을 더해 j 인덱스에 넣고, j+1 인덱스는 제거
            # [3, 2, 2, 3]
            # j값에 변화가 없으므로 제자리에서 다시 해당 과정을 진행
                if len(for_ans_list) == j+1:
                    break
            else:
                j += 1
            # 인접한 구간 사이의 거리의 합이 K보다 큰 경우 값을 그대로 두고 인덱스를 의미하는 j값에 1을 추가함
                if len(for_ans_list) == j+1:
                    break
            # 인덱스 j가 마지막 값일때 리스트는 j+1개의 값을 가지므로, 해당 상황에서 반복문을 탈출

    if ans == -1:
        print(f'#{i+1} {0}')
        # 버스가 지나갈 수 없는 경우

    else:
        print(f'#{i+1} {len(for_ans_list) - 1}')
        # 처음 한번 충전하고 오기때문에 -1을 해줌
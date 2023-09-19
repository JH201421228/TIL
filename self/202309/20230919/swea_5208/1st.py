import sys
sys.stdin = open('input.txt')


def idiot_bus(start, gas, cnt):
    if start + gas >= station_num - 1:
        global ans
        ans = cnt
        return

    max_gas = 0 # 교체할 배터리 변수 선언
    dist = 0 # 거리에 따른 가중치 선언
    next_idx = 0 # 다음 좌표 선언
    max_gas_now = 0 # 가중치를 더한 비교용도의 배터리 변수 선언
    for idx in range(start + 1, start + gas + 1): # 현재 위치에서 배터리가 소모되기 전까지 갈 수 있는 범위
        if station_list[idx] + dist >= max_gas_now: # 배터리 용량에 가중치를 더한 값을 비교
            max_gas_now = station_list[idx] + dist # 비교를 위해 배터리 용량에 가중치를 더해줌
            max_gas = station_list[idx] # 가장 멀리 갈 수 있는 배터리 용량을 기록
            next_idx = idx # 그 때의 좌표를 기록
        dist += 1 # 가중치
    # print(next_idx, max_gas, cnt + 1)
    idiot_bus(next_idx, max_gas, cnt + 1) # 다음 좌표와 배터리 용량을 가지고 함수를 돕시다

T = int(input())
for test in range(T):
    station_list = list(map(int, input().split()))
    station_num = station_list.pop(0)
    # print(station_list)
    # 충전한 위치에 갈 수 있는 범위 안의 가장 큰 값을 선택
    # 해당 행위를 반복
    ans = 0
    idiot_bus(0, station_list[0], 0)
    print(f'#{test+1} {ans}')
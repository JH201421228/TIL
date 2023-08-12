# 삼성시의 버스 노선
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    bus_num = int(input())
    bus_list = [list(map(int, input().split())) for _ in range(bus_num)]

    bus_list_linear = [0]*5001
    for bus_status in bus_list:
        for point in range(bus_status[0], bus_status[1] + 1):
            bus_list_linear[point] += 1

    station_num = int(input())
    station_list = []
    for num in range(station_num):
        station_list.append(bus_list_linear[int(input())])

    print(f'#{test_case + 1}', end= ' ')
    print(*station_list)
# def bus_station_checker(bus_status, station_list):
#     max_station = bus_status[1]
#     min_station = bus_status[0]
#     cnt = 0
#     for station in station_list:
#         if min_station <= station <= max_station:
#             cnt += 1
#     return cnt
#
# Test_Case = int(input())
#
# for test_case in range(Test_Case):
#     bus_num = int(input())
#     bus_list = [list(map(int, input().split())) for _ in range(bus_num)]
#
#     station_num = int(input())
#     station_list = []
#     for num in range(station_num):
#         station_list.append(int(input()))



# Test_Case = int(input())
#
# for test_case in range(Test_Case):
#     bus_num = int(input())
#     bus_list = [list(map(int, input().split())) for _ in range(bus_num)]
#
#     station_num = int(input())
#     station_list = []
#     for num in range(station_num):
#         station_list.append(int(input()))
#
#     print(f'#{test_case + 1}', end= ' ')
#
#     for station in station_list:
#         cnt = 0
#         for bus_status in bus_list:
#             if bus_status[0] <= station <= bus_status[1]:
#                 cnt += 1
#         print(cnt, end= ' ')
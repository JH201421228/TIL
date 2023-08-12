import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    K, N, M = map(int, input().split())
    station_list = list(map(int, input().split()))
    now = 0
    station_num = 0

    while True:

        if station_list[station_num] - now > K:
            break
        elif station_list[station_num] - now <= K:
            now = station_list[station_num]
            station_num += 1


import sys
sys.stdin =open('input.txt')


def idiot_bus(start, gas, cnt, station_num):
    if start + gas >= station_num - 1:
        ans_list.append(cnt)
        return
    if ans_list and cnt > min(ans_list):
        return

    for idx in range(start + 1, start + gas + 1):
        idiot_bus(idx, station_list[idx], cnt + 1, station_num)

T = int(input())
for test in range(T):
    station_list = list(map(int, input().split()))
    station_num = station_list.pop(0)
    ans_list = []
    idiot_bus(0, station_list[0], 0, station_num)
    print(f'#{test+1} {min(ans_list)}')
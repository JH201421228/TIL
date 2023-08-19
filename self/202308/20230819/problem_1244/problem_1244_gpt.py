import sys
sys.stdin = open('input.txt')

switch_num = int(input())
switch_status = list(map(int, input().split()))
students_num = int(input())
students_info = []

for _ in range(students_num):
    students_info.append(list(map(int, input().split())))

for info in students_info:
    if info[0] == 1:
        for idx in range(info[1] - 1, switch_num, info[1]):
            switch_status[idx] = 1 - switch_status[idx]
    else:
        idx = info[1] - 1
        switch_status[idx] = 1 - switch_status[idx]
        di = 1
        while (idx - di >= 0) and (idx + di < switch_num):
            if switch_status[idx - di] == switch_status[idx + di]:
                switch_status[idx - di] = 1 - switch_status[idx - di]
                switch_status[idx + di] = 1 - switch_status[idx + di]
                di += 1
            else:
                break

# 스위치 상태 출력
for i, status in enumerate(switch_status):
    print(status, end=' ')
    if (i + 1) % 20 == 0:  # 매 20개 스위치마다 줄 바꿈
        print()

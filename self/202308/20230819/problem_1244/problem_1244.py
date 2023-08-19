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
        for idx in range(switch_num):
            if not (idx + 1) % info[1]:
                if switch_status[idx]:
                    switch_status[idx] = 0
                else:
                    switch_status[idx] = 1
    else:
        idx = info[1] - 1
        di = 1
        if switch_status[idx]:
            switch_status[idx] = 0
        else:
            switch_status[idx] = 1
        while True:
            if 0 <= idx - di and idx + di < switch_num:
                if switch_status[idx-di] == switch_status[idx+di]:
                    if switch_status[idx-di]:
                        switch_status[idx - di] = switch_status[idx + di] = 0
                    else:
                        switch_status[idx - di] = switch_status[idx + di] = 1
                    di += 1
                else:
                    break
            else:
                break

# print(switch_status)
for i in range(switch_num):
    if not i or i % 20:
        print(switch_status[i], end=' ')
    else:
        print()
        print(switch_status[i], end=' ')

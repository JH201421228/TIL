import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    move_student = int(input())
    room_info = []
    for _ in range(move_student):
        room_info.append(list(map(int, input().split())))

    trace_list = [0] * 200

    for inner_list in room_info:
        for index in range((min(inner_list) - 1)//2, (max(inner_list) - 1)//2 + 1):
            trace_list[index] += 1

    print(f'#{test_case + 1} {max(trace_list)}')
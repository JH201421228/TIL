import sys
sys.stdin = open('input.txt')

stu_num, room_maxi = map(int, input().split())
ans_list = [[0, 0] for _ in range(6)]
for _ in range(stu_num):
    se, grade = map(int, input().split())
    if se:
        ans_list[grade-1][1] += 1
    else:
        ans_list[grade-1][0] += 1
# print(ans_list)
total_room = 0
for inner in ans_list:
    if inner[0]:
        total_room += (inner[0] - 1) // room_maxi + 1
    if inner[1]:
        total_room += (inner[1] - 1) // room_maxi + 1
print(total_room)
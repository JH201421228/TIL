import sys
sys.stdin = open('input.txt')


def find_height_sum_100(start):
    if sum(ans) == 100 and len(ans) == 7:
        ans_list.append(ans[:])
        return
    elif sum(ans) > 100:
        return
    elif len(ans) > 7:
        return

    for i in range(start, 9):
        ans.append(height[i])
        find_height_sum_100(i+1)
        ans.pop()


height = []
for _ in range(9):
    height.append(int(input()))
# print(height)
height.sort()
ans = []
ans_list = []
find_height_sum_100(0)
if ans_list:
    # ans_list[0].sort()
    for num in ans_list[0]:
        print(num)
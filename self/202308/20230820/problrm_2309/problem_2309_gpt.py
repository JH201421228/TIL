import sys
sys.stdin = open('input.txt')

def find_height_sum_100(start, current_sum):
    if current_sum == 100:
        ans_list.append(ans[:])
        return
    elif current_sum > 100:
        return

    for i in range(start, 9):
        ans.append(height[i])
        find_height_sum_100(i + 1, current_sum + height[i])
        ans.pop()

height = []
for _ in range(9):
    height.append(int(input()))

height.sort()
ans = []
ans_list = []
find_height_sum_100(0, 0)

if ans_list:
    for num in ans_list[0]:
        print(num)
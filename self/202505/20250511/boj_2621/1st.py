import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


color_idx = {'R': 0, 'B': 1, 'Y': 2, 'G': 3}
colors = [0] * 4
nums = [0] * 10
nums_list = []

for _ in range(5):
    color, num = map(str, input().rstrip().split())

    colors[color_idx[color]] += 1
    nums[int(num)] += 1
    nums_list.append(int(num))

max_color = max(colors)
max_num = max(nums)
nums_list.sort()

# 900
is_nine_hundred = True
for idx in range(1, 5):
    if nums_list[idx] == nums_list[idx-1]+1:
        continue
    is_nine_hundred = False
    break

if max_color == 5 and is_nine_hundred:
    print(900 + max(nums_list))
    exit(0)

# 800
if max_num == 4:
    for idx in range(1, 10):
        if nums[idx] == 4:
            print(800 + idx)
            exit(0)

# 700
three, two, twos = 0, 0, []
for idx in range(1, 10):
    if nums[idx] == 2:
        two = idx
        twos.append(idx)
    elif nums[idx] == 3:
        three = idx

if two and three:
    print(700 + three*10 + two)
    exit(0)

# 600
if max_color == 5:
    print(600 + max(nums_list))
    exit(0)

# 500
if is_nine_hundred:
    print(500 + max(nums_list))
    exit(0)

# 400
if three:
    print(400 + three)
    exit(0)

# 300
if len(twos) == 2:
    print(300 + max(twos)*10 + min(twos))
    exit(0)

# 200
if two:
    print(200 + two)
    exit(0)

# 100
print(100 + max(nums_list))
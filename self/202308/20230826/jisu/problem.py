import sys
sys.stdin = open('input.txt')

N = int(input()) # 참외 갯수
yellow_melon = [list(map(int, input().split())) for _ in range(6)]

# 다음 값 나오면 회전하면됨
area = [[0]*201 for _ in range(201)]

y = 0
x = 0
list_x = []
list_y = []
cnt = 0
for key, value in yellow_melon:
    # print(key, value)
    for i in range(value-1):
        # print(i,'i')
        # print(x, y, 'xy')
        if key == 4:
            if area[y][x] != 1:
                area[y][x] = 1
                y += 1
                cnt += 1
                list_y.append(value)
        # print(y,'y')
        if key == 2:
            if area[y][x] != 1:
                area[y][x] = 1
                x += 1
                cnt += 1
                list_x.append(value)
        # print(x,'x')
        if key == 3:
            if area[y][x] != 1:
                area[y][x] = 1
                y -= 1
                cnt += 1
                list_y.append(value)
        # print(y,'y')
        if key == 1:
            if area[y][x] != 1:
                area[y][x] = 1
                x -= 1
                cnt += 1
                list_x.append(value)
        # print(x,'x')
# print(area)
# print(max(list_x),max(list_y))
# for inner in area:
#     print(inner.count(1))
for i in range(0,max(list_y)):
    for j in range(1,max(list_x)):
        if area[i][j] != 1 and area[i][j-1] == 1:
            area[i][j] = 1
            # print(j)
            cnt += 1
        else:
            break

# print(area[0].count(1),area[30].count(1))
print(cnt *N,cnt)
import sys
sys.stdin = open('input.txt')


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def find_find(x, y, num):
    how_many_room = 0

    while True:
        for dx, dy in delta:
            if 0 <= x+dx < N and 0 <= y+dy < N and room[x+dx][y+dy] == room[x][y] + 1:
                how_many_room += 1
                x = x+dx
                y = y+dy
                break
        else:
            break
    return [how_many_room, num]



T = int(input())
for test in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # print(room)
    ans_list = []
    for i in range(N):
        for j in range(N):
            ans_list.append(find_find(i, j, room[i][j]))
    ans_list.sort(key=lambda x:(x[0], -x[1]))
    print(f'#{test+1} {ans_list[-1][1]} {ans_list[-1][0] + 1}')
    # print()
    # print('--------------------')
    # # print(ans_list)



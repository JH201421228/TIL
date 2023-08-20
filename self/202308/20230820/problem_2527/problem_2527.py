import sys
sys.stdin = open('input.txt')


for _ in range(4):
    square_info = list(map(int, input().split()))
    x_line = [0] * 50001
    y_line = [0] * 50001
    square1 = square_info[:4] # x1, y1, x2, y2
    square2 = square_info[4:]
    for i in range(2):
        x_line[square1[2 * i]] += 1
        x_line[square2[2 * i]] += 2
        y_line[square1[2 * i + 1]] += 1
        y_line[square2[2 * i + 1]] += 2
    x_list = []
    y_list = []
    for i in x_line:
        if i:
            x_list.append(i)
    for i in y_line:
        if i:
            y_list.append(i)

    not_tangled1 = [1, 1, 2, 2]
    not_tangled2 = [2, 2, 1, 1]
    # if len(x_list) == 3 and len(y_list) == 3:
    #     print('c')
    # elif (len(x_list) == 3 and y_list != not_tangled1 and y_list != not_tangled2) or (len(y_list) == 3 and x_list != not_tangled1 and x_list != not_tangled2):
    #     print('b')
    # elif (x_list != not_tangled1 and x_list != not_tangled2) and (y_list != not_tangled1 and y_list != not_tangled2):
    #     print('a')
    # else:
    #     print('d')
    if len(x_list) == 2 and len(y_list) == 2:
        print('')
    elif len(x_list) == 3 and len(y_list) == 3 and (x_list[1] == 3 and y_list[1] == 3):
        print('c')
    elif len(x_list) == 3 and len(y_list) == 3 and (x_list[1] != 3 and y_list[1] != 3):
        print('a')
    elif (len(x_list) == 3 and y_list != not_tangled1 and y_list != not_tangled2) or (len(y_list) == 3 and x_list != not_tangled1 and x_list != not_tangled2):
        print('b')
    elif (x_list == not_tangled1 or x_list == not_tangled2) or (y_list == not_tangled1 or y_list == not_tangled2):
        print('d')
    else:
        print('a')
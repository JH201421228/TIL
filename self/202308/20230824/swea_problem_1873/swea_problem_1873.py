import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    H, W = map(int, input().split())
    mapp = [list(map(str, input())) for _ in range(H)]
    commend_num = int(input())
    commend = list(map(str, input()))

    # 전차 위치 설정
    flag = 0
    status = '<>^v'
    for i in range(H):
        for j in range(W):
            if mapp[i][j] in status:
                start_i = i
                start_j = j
                flag = 1
                break
        if flag:
            break

    # print(start_i, start_j)
    # 게임 시작
    i_idx = start_i
    j_idx = start_j
    while commend:
        now = commend.pop(0)
        if now == 'U':
            mapp[i_idx][j_idx] = '^'
            if 0 <= i_idx - 1 and mapp[i_idx - 1][j_idx] == '.':
                mapp[i_idx][j_idx] = '.'
                i_idx = i_idx - 1
                mapp[i_idx][j_idx] = '^'
        elif now == 'D':
            mapp[i_idx][j_idx] = 'v'
            if i_idx + 1 < H and mapp[i_idx + 1][j_idx] == '.':
                mapp[i_idx][j_idx] = '.'
                i_idx = i_idx + 1
                mapp[i_idx][j_idx] = 'v'
        elif now == 'L':
            mapp[i_idx][j_idx] = '<'
            if 0 <= j_idx - 1 and mapp[i_idx][j_idx - 1] == '.':
                mapp[i_idx][j_idx] = '.'
                j_idx = j_idx - 1
                mapp[i_idx][j_idx] = '<'
        elif now == 'R':
            mapp[i_idx][j_idx] = '>'
            if j_idx + 1 < W and mapp[i_idx][j_idx + 1] == '.':
                mapp[i_idx][j_idx] = '.'
                j_idx = j_idx + 1
                mapp[i_idx][j_idx] = '>'

        elif now == 'S':
            status = mapp[i_idx][j_idx]
            s_i = i_idx
            s_j = j_idx
            if status == '^':
                for _ in range(H):
                    s_i -= 1
                    if s_i < 0:
                        break
                    elif mapp[s_i][s_j] == '*':
                        mapp[s_i][s_j] = '.'
                        break
                    elif mapp[s_i][s_j] == '#':
                        break
            elif status == 'v':
                for _ in range(H):
                    s_i += 1
                    if s_i >= H:
                        break
                    elif mapp[s_i][s_j] == '*':
                        mapp[s_i][s_j] = '.'
                        break
                    elif mapp[s_i][s_j] == '#':
                        break
            elif status == '<':
                for _ in range(W):
                    s_j -= 1
                    if s_j < 0:
                        break
                    elif mapp[s_i][s_j] == '*':
                        mapp[s_i][s_j] = '.'
                        break
                    elif mapp[s_i][s_j] == '#':
                        break
            elif status == '>':
                for _ in range(W):
                    s_j += 1
                    if s_j >= W:
                        break
                    elif mapp[s_i][s_j] == '*':
                        mapp[s_i][s_j] = '.'
                        break
                    elif mapp[s_i][s_j] == '#':
                        break
        # print(now)
    print(f'#{test + 1}', end=' ')
    for inner in mapp:
        print(''.join(inner))
        # print('-------------')

import sys
sys.stdin = open('input.txt')


def why_do_this(check_num, now_num, out_idx):

    if check_num == change_num:
        global max_val
        if now_num > max_val:
            max_val = now_num
        return

    if now_num == ultimate_num:
        ans_list.append(([now_num, check_num]))
        return

    if out_idx <= len(integer_list) - 2:
        while max(integer_list[out_idx:]) == integer_list[out_idx]:
            out_idx += 1

    for idx in range(out_idx, len(integer_list)):
        if max(integer_list[out_idx:]) == integer_list[idx]:
            integer_list[out_idx], integer_list[idx] = integer_list[idx], integer_list[out_idx]
            why_do_this(check_num+1, int(''.join(integer_list)), out_idx+1)
            integer_list[out_idx], integer_list[idx] = integer_list[idx], integer_list[out_idx]


T = int(input())
for test in range(T):
    integer, change_num = map(int, input().split())
    integer_list = list(map(str, str(integer)))
    # print(integer_list)
    copy_cat = integer_list[:]
    copy_cat.sort(reverse=True)
    ultimate_num = int(''.join(copy_cat))
    ans_list = []
    max_val = 0

    # print(ultimate_num)
    # for inner in integer_list:
    #     print(type(inner))
    why_do_this(0, int(''.join(integer_list)), 0)
    # print(max_val)
    # print(ans_list)
    if not ans_list:
        print(f'#{test+1} {max_val}')
    else:
        if len(set(integer_list)) != len(integer_list):
            print(f'#{test+1} {ans_list[0][0]}')
        else:
            if (change_num - ans_list[0][1]) % 2:
                copy_cat[-1], copy_cat[-2] = copy_cat[-2], copy_cat[-1]
                print(f"#{test+1} {int(''.join(copy_cat))}")
            else:
                print(f"#{test+1} {int(''.join(copy_cat))}")
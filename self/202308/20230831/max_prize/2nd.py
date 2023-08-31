import sys
sys.stdin = open('input.txt')

def this_problem_is_suck(check_num, this_integer, out_idx, ultimate_val):
    # 교환 횟수가 되면 비교
    # 더 작은 수가 되면 변경
    # 그리고 나서 리턴
    if this_integer == ultimate_val:
        ans_list.append([check_num, this_integer])
        return

    if check_num == change_num:
        global max_integer
        if this_integer > max_integer:
            max_integer = this_integer
        return

    while max(integer_list[out_idx:]) == integer_list[out_idx]:
        if integer_list[out_idx:].count(max(integer_list[out_idx:])) > 1:
            break
        out_idx += 1
        if out_idx >= len(integer_list):
            break

    for idx in range(out_idx + 1, len(integer_list)):
        integer_list[out_idx], integer_list[idx] = integer_list[idx], integer_list[out_idx]
        this_problem_is_suck(check_num + 1, int(''.join(integer_list)), out_idx + 1, ultimate_val)
        integer_list[out_idx], integer_list[idx] = integer_list[idx], integer_list[out_idx]


T = int(input())
for test in range(T):
    integer, change_num = map(int, input().split())
    integer_list = list(map(str, str(integer)))
    max_integer = 0
    # print(integer_list)
    # for num in integer_list:
    #     print(num, type(num))
    copy_cat = integer_list[:]
    copy_cat.sort(reverse=True)
    ultimate_val = int(''.join(copy_cat))
    ans_list = []
    #
    # if change_num >= len(integer_list) - 1:
    #     integer_list.sort(reverse=True)
    #     if len(integer_list) != len(set(integer_list)):
    #         print(f"#{test + 1} {''.join(integer_list)}")
    #     elif not (change_num - len(integer_list)) % 2:
    #         print(f"#{test + 1} {''.join(integer_list)}")
    #     else:
    #         integer_list[-1], integer_list[-2] = integer_list[-2], integer_list[-1]
    #         print(f"#{test + 1} {''.join(integer_list)}")
    # else:
    this_problem_is_suck(0, int(''.join(integer_list)), 0, ultimate_val)
    if not ans_list:
        print(f'#{test+1} {max_integer}')
    elif ans_list[0][0] == change_num:
        print(f'#{test+1} {ultimate_val}')
    else:
        if len(integer_list) != len(set(integer_list)):
            print(f'#{test+1} {ultimate_val}')
        elif (change_num - ans_list[0][0]) % 2:
            copy_cat[-1], copy_cat[-2] = copy_cat[-2], copy_cat[-1]
            print(f"#{test+1} {''.join(copy_cat)}")
        else:
            print(f"#{test+1} {''.join(copy_cat)}")

    # print(f'#{test + 1} {max_integer}')
    # print(ans_list)
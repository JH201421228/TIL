import sys
sys.stdin = open('input.txt')


def this_game(check_plz):
    my_list = check_plz[:]
    my_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in my_list:
        my_dict[num] += 1
        if my_dict[num] == 3:
            return True
    # print(my_dict)
    # print(my_list)

    my_list = list(set(my_list))
    my_list.sort()
    # print(my_list)
    conti = 0
    for idx in range(len(my_list) - 1):
        if my_list[idx+1] == my_list[idx] + 1:
            conti += 1
        else:
            conti = 0
        if conti == 2:
            return True

    return False


T = int(input())
for test in range(T):
    cards = list(map(int, input().split()))
    # print(cards)
    player_A = []
    player_B = []
    for _ in range(2):
        player_A.append(cards.pop(0))
        player_B.append(cards.pop(0))

    while cards:
        player_A.append(cards.pop(0))
        result_A = this_game(player_A)
        if result_A:
            print(f'#{test + 1} 1')
            break

        player_B.append(cards.pop(0))
        result_B = this_game(player_B)
        if result_B:
            print(f'#{test + 1} 2')
            break

    if not result_A and not result_B:
        print(f'#{test + 1} 0')
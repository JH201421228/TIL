import sys
sys.stdin = open('input.txt')


def this_game_is_terrible(someones_cards):
    check_card = someones_cards[:]
    dic = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in check_card:
        dic[num] += 1
        if dic[num] == 3:
            # print('dict')
            return True

    check_card = list(set(check_card))
    check = 0
    for idx in range(len(check_card) - 1):
        if check_card[idx + 1] - check_card[idx] == 1:
            check += 1
        else:
            check = 0
        if check >= 2:
            # print('gin')
            return True

    return False


T = int(input())
for test in range(T):
    cards = list(map(int, input().split()))
    player_A = []
    player_B = []
    player_A.append(cards.pop(0))
    player_B.append(cards.pop(0))
    player_A.append(cards.pop(0))
    player_B.append(cards.pop(0))

    check = 0
    while cards:
        player_A.append(cards.pop(0))
        result_A = this_game_is_terrible(player_A)
        if result_A:
            print(f'#{test+1} 1')
            check = 1
            break

        player_B.append(cards.pop(0))
        result_B = this_game_is_terrible(player_B)
        if result_B:
            print(f'#{test+1} 2')
            check = 1
            break
    else:
        print(f'#{test+1} 0')


    # dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    # dict[1] += 1
    # print(dict)



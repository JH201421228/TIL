import sys
sys.stdin = open('input.txt')


def this_game_is_terrible(someones_cards):
    check_cards = someones_cards[:]
    dictt = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in check_cards:
        dictt[num] += 1
        if dictt[num] == 3:
            return True

    check_cards = list(set(check_cards))
    check_cards.sort()
    check = 0
    for idx in range(len(check_cards) - 1):
        if check_cards[idx + 1] - check_cards[idx] == 1:
            check += 1
        else:
            check = 0
        if check == 2:
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
    while cards:
        player_A.append(cards.pop(0))
        result_A = this_game_is_terrible(player_A)
        if result_A:
            print(f'#{test+1} 1')
            break
        player_B.append(cards.pop(0))
        result_B = this_game_is_terrible(player_B)
        if result_B:
            print(f'#{test+1} 2')
            break
        # if result_A or result_B:
        #     if result_A and result_B:
        #         print(f'#{test+1} 0')
        #         break
        #     elif result_A:
        #         print(f'#{test+1} 1')
        #         break
        #     else:
        #         print(f'#{test+1} 2')
        #         break
    if not result_A and not result_B:
        print(f'#{test+1} 0')
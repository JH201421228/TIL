import sys
input = sys.stdin.readline

have_card_num = int(input())
have_card_list = list(map(int, input().split()))
have_card_dict = {}

for card in have_card_list:
    have_card_dict[card] = have_card_dict.get(card, 0) + 1

check_card_num = int(input())
check_card_list = list(map(int, input().split()))
ans_list = []

for card in check_card_list:
    ans_list.append(have_card_dict.get(card, 0))

print(*ans_list)
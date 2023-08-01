Test_case = int(input())

for test_case in range(Test_case):
    num_of_card = int(input())
    card_list_str = input()
    card_list = []

    for char in card_list_str:
        card_list.append(int(char))

    # print(card_list)

    card_dict = {}

    for char in card_list:
        card_dict[char] = card_dict.get(char, 0) + 1

    # print(card_dict)

    ans_card = card_list[0]
    ans_num = 0

    for card, num in card_dict.items():
        if num == ans_num:
            if card > ans_card:
                ans_card = card
                ans_num = num
        elif num > ans_num:
            ans_card = card
            ans_num = num

    print(f'#{test_case+1} {ans_card} {ans_num}')
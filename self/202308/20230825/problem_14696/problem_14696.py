import sys
sys.stdin = open('input.txt')

# 우선순위 별, 동그라미, 네모, 세모
battle = int(input())
for _ in range(battle):
    A_card = [0] * 5
    B_card = [0] * 5
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))
    for idx in range(1, len(A_list)):
        A_card[A_list[idx]] += 1
    for idx in range(1, len(B_list)):
        B_card[B_list[idx]] += 1

    A = A_card.pop(0)
    B = B_card.pop(0)
    while True:
        A = A_card.pop()
        B = B_card.pop()

        if A > B:
            print('A')
            break
        elif B > A:
            print('B')
            break

        if not A_card and not B_card:
            print('D')
            break
        elif not A_card:
            print('B')
            break
        elif not B_card:
            print('A')
            break
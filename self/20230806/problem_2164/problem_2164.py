import sys
from collections import deque

# sys.stdin = open('input.txt')
# input = sys.stdin.readline()

N = int(input())

card_list = deque(list(i for i in range(1, N + 1)))
turn = 1
while len(card_list) > 1:
    if turn % 2:
        card_list.popleft()
        turn += 1
    else:
        card = card_list.popleft()
        card_list.append(card)
        turn += 1

print(*card_list)
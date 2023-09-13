import sys

sys.stdin = open('input.txt')

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def what_the_game():



R, C = map(int, input().split())
board_info = [list(input()) for _ in range(R)]
trace = [board_info[0][0]]
board_info[0][0] = 0
what_the_game()
print(board_info)
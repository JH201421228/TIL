import sys
sys.stdin = open('input.txt')
for _ in range(4):
    square_info = [list(map(int, input().split())) for _ in range(2)]
    print(square_info)
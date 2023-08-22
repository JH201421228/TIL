import sys
sys.stdin = open('input.txt')

# 세로 1, 가로 0
horizon, vertical = map(int, input().split())
cutting_num = int(input())
cutting_info = [list(map(int, input().split())) for _ in range(cutting_num)]
print(cutting_info)



import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    order_num = int(input())
    order_info = [list(map(int, input().split())) for _ in range(order_num)]
    order_info.sort(key=lambda x: x[1])

    for i in range(1, order_info):
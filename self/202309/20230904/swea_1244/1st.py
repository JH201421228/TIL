import sys
sys.stdin = open('input.txt')


def findfind():




T = int(input())
for test in range(T):
    num, change = map(str, input().split())
    change = int(change)
    num_list = list(map(int, num))
    # print(num_list)

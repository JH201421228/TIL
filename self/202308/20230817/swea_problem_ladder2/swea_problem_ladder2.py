import sys
sys.stdin = open('input.txt')


def let_s_go(start):
    pass


for _ in range(10):
    test_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if ladder[0][i]:
            start.append(i)
    print(start)

import sys
sys.stdin = open('input.txt')


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = list(map(int, input().split()))
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')
    elif p1 == x2 or p2 == x1:
        if q1 == y2 or q2 == y1:
            print('c')
        else:
            print('b')
    elif q1 == y2 or q2 == y1:
        print('b')
    else:
        print('a')
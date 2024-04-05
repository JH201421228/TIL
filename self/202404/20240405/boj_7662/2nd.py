import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    q = []
    add_cnt = 0
    out_cnt = 0
    log = []
    for _ in range(int(input())):
        a, b = input().rstrip().split()
        if a == 'I':
            q.append(int(b))
            log.append('I')
        elif a == 'D':
            if not log:
                continue
            else:
                if log[-1] == 'I':
                    q.sort()
                if q and int(b) == 1:
                    del q[-1]
                elif q and int(b) == -1:
                    del q[0]
    if q:
        print(q[-1], q[0])
    else:
        print('EMPTY')
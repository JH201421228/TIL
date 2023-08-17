import sys
sys.stdin = open('input.txt')


def let_s_go(start):
    ans = 0
    x = 0
    y = start

    while True:
        if 0 <= y-1 and ladder[x][y-1] and status != -1:
            y = y-1
            ans += 1
            status = 1
        elif y+1 < 100 and ladder[x][y+1] and status != 1:
            y = y+1
            ans += 1
            status = -1
        else:
            x = x+1
            ans += 1
            status = 0
            if x == 99:
                return ans


for _ in range(10):
    test_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if ladder[0][i]:
            start.append(i)

    ans = []
    for i in start:
        ans.append(let_s_go(i))
    print(f'#{test_num} {start[ans.index(min(ans))]}')
import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            if warehouse[i][j]:
                x1 = i
                x2 = i
                y1 = j
                y2 = j
                ans.append([x1, y1])
                while True:
                    y2 += 1
                    if not warehouse[i][y2]:
                        break
                while True:
                    x2 += 1
                    if not warehouse[x2][y2-1]:
                        break
                ans.append([x2, y2])

                for x in range(x1, x2):
                    for y in range(y1, y2):
                        warehouse[x][y] = 0
    ans_num = len(ans)//2
    sorted_list = []
    for i in range(ans_num):
        x1, y1 = ans[2*i]
        x2, y2 = ans[2*i + 1]
        sorted_list.append([(x2-x1)*(y2-y1), x2-x1, y2-y1])
        sorted_list.sort()
    print(f'#{test+1} {ans_num}', end=' ')
    for i, j, k in sorted_list:
        print(j, k, end=' ')
    print()
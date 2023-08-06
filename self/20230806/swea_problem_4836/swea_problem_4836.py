import sys
sys.stdin = open('input.txt')


Test_Case = int(input())

for test_case in range(Test_Case):
    paper = [[0] * 10 for _ in range(10)]
    color_num = int(input())

    for _ in range(color_num):
        x_start, y_start, x_end, y_end, color = map(int, input().split())
        for x_index in range(x_start, x_end + 1):
            for y_index in range(y_start, y_end + 1):
                if paper[x_index][y_index] == 0 or paper[x_index][y_index] != color:
                    paper[x_index][y_index] += color
    cnt = 0
    for x_index in range(10):
        for y_index in range(10):
            if paper[x_index][y_index] >= 3:
                cnt += 1
    print(f'#{test_case + 1} {cnt}')

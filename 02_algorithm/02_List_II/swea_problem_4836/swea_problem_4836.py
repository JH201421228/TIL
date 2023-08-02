import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    total_list = [[0] * 10 for _ in range(10)]
    color_num = int(input())
    cordinate_and_color = []

    for num in range(color_num):
        cordinate_and_color.append(list(map(int, input().split())))

    for i_start, j_start, i_end, j_end, color in cordinate_and_color:
        for i in range(i_start, i_end+1):
            for j in range(j_start, j_end+1):
                if total_list[i][j] == 0 or total_list[i][j] != color or total_list[i][j] != 3:
                    total_list[i][j] += color
    ans = 0
    for i in range(10):
        for j in range(10):
            if total_list[i][j] == 3:
                ans += 1
    print(f'#{test_case+1} {ans}')
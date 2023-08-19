import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    farm_size = int(input())
    farm_info = [list(map(int, input())) for _ in range(farm_size)]
    ans = 0
    for i in range(farm_size):
        start = farm_size//2 - i
        end = farm_size//2 + i + 1
        if start < 0:
            start = -start
        if end > farm_size:
            end = farm_size * 2 - end
        for j in range(start, end):
            ans += farm_info[i][j]

    print(f'#{test+1} {ans}')
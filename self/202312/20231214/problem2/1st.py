import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for _ in range(10):
    t = int(input())

    ans = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            sum1 += arr[i][j]
            sum2 += arr[j][i]

        ans = max(ans, sum1, sum2)

        sum1 = 0
        sum2 = 0
        sum3 += arr[i][i]
        sum4 += arr[i][99-i]

    ans = max(ans, sum3, sum4)

    print(f'#{t} {ans}')
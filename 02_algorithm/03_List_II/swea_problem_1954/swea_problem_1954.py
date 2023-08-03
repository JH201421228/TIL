import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    scale_of_matrix = int(input())
    ans_matrix = [[0]*scale_of_matrix for _ in range(scale_of_matrix)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = 0
    cordinate = 0

    for i in range(1, scale_of_matrix**2 + 1):
        ans_matrix[x][y] = i

        if x+dx[cordinate] < 0 or x+dx[cordinate] >= scale_of_matrix or y+dy[cordinate] < 0 or y+dy[cordinate] >= scale_of_matrix or ans_matrix[x+dx[cordinate]][y+dy[cordinate]] != 0:
            cordinate = (cordinate + 1) % 4

        x += dx[cordinate]
        y += dy[cordinate]

    print(f'#{test_case+1}')
    for i in range(len(ans_matrix)):
        print(*ans_matrix[i])




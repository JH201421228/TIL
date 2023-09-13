import sys
sys.stdin = open('input.txt')


N = int(input())
ans_list = [[0]*10 for _ in range(100)]
for idx in range(1,10):
    ans_list[0][idx] = 1
for i in range(1, N):
    for j in range(10):
        if not j:
            ans_list[i][j] = ans_list[i-1][1]
        elif j == 9:
            ans_list[i][j] = ans_list[i-1][8]
        else:
            ans_list[i][j] = ans_list[i-1][j-1] + ans_list[i-1][j+1]
print(sum(ans_list[N-1]) % 1000000000)
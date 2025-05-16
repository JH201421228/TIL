import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

MOD = 987_654_321

N = int(input())

arr = [[0] * 9 for _ in range(N)]
arr[0] = [1] * 9

for idx in range(N-1):
    for i in range(9):
        for di in range(-2, 3):
            if i+di >= 0 and i+di < 9:
                arr[idx+1][i+di] += arr[idx][i]
                arr[idx+1][i+di] %= MOD

print(sum(arr[-1]) % MOD)
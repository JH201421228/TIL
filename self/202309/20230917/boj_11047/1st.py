import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
ans = 0
while K:
    for idx in range(-1, -(N+1), -1):
        ans += K//coin_list[idx]
        K %= coin_list[idx]
print(ans)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = sum(arr[:K])
temp = ans
cnt = 1

for idx in range(K, N):
    temp += arr[idx]
    temp -= arr[idx-K]

    if temp >= ans:
        if ans == temp: cnt += 1
        else:
            ans = temp
            cnt = 1

if ans:
    print(ans)
    print(cnt)
else: print("SAD")
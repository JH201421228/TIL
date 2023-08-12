N, K = map(int, input().split())
ans_list = []

for i in range(1, N + 1):
    if N % i == 0:
        ans_list.append(i)

try:
    print(ans_list[K - 1])
except:
    print(0)
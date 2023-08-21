import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
temp_list = list(map(int, input().split()))
first = sum(temp_list[:K])
ans = [first]
for idx in range(K, N):
    first = first + temp_list[idx] - temp_list[idx - K]
    ans.append(first)
print(max(ans))

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


T = int(input())
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_dict = dict()
for idx in range(1, N):
    N_list[idx] += N_list[idx-1]
for idx in range(N):
    N_dict[N_list[idx]] = N_dict.get(N_list[idx], 0) + 1

M_dict = dict()
for idx in range(1, M):
    M_list[idx] += M_list[idx-1]
for idx in range(M):
    M_dict[M_list[idx]] = M_dict.get(M_list[idx], 0) + 1

for i in range(N-1):
    for j in range(i+1, N):
        N_dict[N_list[j] - N_list[i]] = N_dict.get(N_list[j] - N_list[i], 0) + 1

for i in range(M-1):
    for j in range(i+1, M):
        M_dict[M_list[j] - M_list[i]] = M_dict.get(M_list[j] - M_list[i], 0) + 1

ans = 0
for key, value in N_dict.items():
    ans += value * M_dict.get(T-key, 0)
print(ans)

# print(N_list)
# print(N_dict)
# print(M_list)
# print(M_dict)
import sys
sys.stdin = open('input.txt')

N = int(input())
check_list = [0] * (N + 1)

for idx in range(2, N+1):
    check_list[idx] = check_list[idx - 1] + 1
    if not idx % 3:
        check_list[idx] = min(check_list[idx], check_list[idx // 3] + 1)
    if not idx % 2:
        check_list[idx] = min(check_list[idx], check_list[idx // 2] + 1)
print(check_list)

check_list = [0] * (N + 1)
for idx in range(2, N+1):
    check_list[idx] = check_list[idx - 1] + 1
    if not idx % 3:
        check_list[idx] = min(check_list[idx - 1], check_list[idx // 3]) + 1
    if not idx % 2:
        check_list[idx] = min(check_list[idx - 1], check_list[idx // 2]) + 1
print(check_list)
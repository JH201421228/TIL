import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

ans = 0
ans_list = []
for i in range(N):
    ans += i
    ans_list.append(1<<i)

print(ans)
print(*ans_list)

ans = -1
ans_list = []
for i in range(N):
    ans += 1
    ans_list.append(i+1)

print(ans)
print(*ans_list)
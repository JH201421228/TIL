import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

total_j, total_i = map(int, input().split())
start_j, start_i = map(int, input().split())
start_i = total_i - start_i
time = int(input())

now_i = start_i
now_j = start_j
di = -1
dj = 1

time = time % (total_i*total_j)

for _ in range(time):

    if (now_i == 0 or now_i == total_i) and (now_j == 0 or now_j == total_j):
        di = -di
        dj = -dj
    elif now_i == 0 or now_i == total_i:
        di = -di
    elif now_j == 0 or now_j == total_j:
        dj = -dj

    now_i += di
    now_j += dj

print(now_j, total_i - now_i)
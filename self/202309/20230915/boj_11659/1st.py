import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
for _ in range(M):
    start_idx, end_idx = map(int, input().split())
    print(sum(num_list[start_idx-1:end_idx]))
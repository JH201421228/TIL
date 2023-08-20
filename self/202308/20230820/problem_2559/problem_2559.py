import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

days, how_day = map(int, input().split())
temp_list = list(map(int, input().split()))
ans = []
for idx in range(days - how_day + 1):
    ans.append(sum(temp_list[idx:idx+how_day]))
print(max(ans))
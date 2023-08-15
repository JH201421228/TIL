import sys
sys.stdin = open('input.txt')

def team_power(arr):
    length = len(arr)
    total = 0
    for i in range(length-1):
        for j in range(i+1, length):
            total += status_matrix[arr[i]-1][arr[j]-1]
            total += status_matrix[arr[j]-1][arr[i]-1]
    return total

def divide_team(N, arr,start):
    if len(arr) == N//2:
        all_team_powers.append(team_power(arr))
        return
    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            divide_team(N, arr, i+1)
            arr.pop()

even_num = int(input())
status_matrix = [list(map(int, input().split())) for _ in range(even_num)]
team_member = []
team_powers = []
all_team_powers = []
start = 1
divide_team(even_num, team_member, start)
length = len(all_team_powers)
min_val = max(all_team_powers)
for i in range(length):
    val = abs(all_team_powers[i] - all_team_powers[-(i+1)])
    if val < min_val:
        min_val = val

print(min_val)
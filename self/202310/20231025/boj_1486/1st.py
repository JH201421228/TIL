import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 현재 위치보다 낮은 곳 및 같은 곳으로 갈 때는 1초의 시간이 걸림
# 반면, 높은 곳으로 갈 때에는 높이 차이의 제곱만큼의 시간이 걸림


N, M, T, D = map(int, input().split())
mountain = [list(input().rstrip()) for _ in range(N)]
print(mountain)
for
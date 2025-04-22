import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]

bucket = []

dots.sort()
print(dots)
for i in range(3):
    bucket.append(max(abs(dots[i][0] - dots[-3+i][0])+2, abs(dots[i][1] - dots[-3+i][1])+2))

dots.sort(key=lambda x : x[1])
print(dots)
for i in range(3):
    bucket.append(max(abs(dots[i][0] - dots[-3+i][0])+2, abs(dots[i][1] - dots[-3+i][1])+2))

print(min(bucket)**2)

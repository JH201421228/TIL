import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, K = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort()
print(scores)


def

start, end =
while start <= mid
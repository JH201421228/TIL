import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    K = int(input())
    arr = [[0] * K for _ in range(K)]
    arr[0] = list(map(int, input().split()))
    for i in range(1, K):
        for j in range(i, K):

    for inner in arr:
        print(inner)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    K = int(input())
    K_list = list(map(int, input().split()))
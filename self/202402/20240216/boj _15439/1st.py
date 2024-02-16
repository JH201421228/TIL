import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
print(n*(n-1))
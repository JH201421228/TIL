import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


n = int(input())
print(2**n)
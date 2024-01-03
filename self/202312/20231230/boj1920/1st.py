import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
N_list = set(map(int, input().split()))


M = int(input())
M_list = list(map(int, input().split()))

for num in M_list:
    if num in N_list:
        print(1)
    else:
        print(0)
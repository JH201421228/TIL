import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 에라토스테네스의 채로 P**0.5 보다 작은 prime num 구함
# 위에서 구한 prime num 으로 P 소인수분해
# https://daebaq27.tistory.com/106
S, P = map(int, input().split())
print(S, P)
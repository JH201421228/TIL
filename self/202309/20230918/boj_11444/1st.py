import sys
import math
sys.stdin = open('input.txt')


n = int(input())

ans = (((1 + math.sqrt(5))/2)**n - ((1 - math.sqrt(5))/2)**n) / math.sqrt(5)
print(int(ans % 1000000007))

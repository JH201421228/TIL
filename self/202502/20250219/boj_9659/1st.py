import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

if int(input()) % 2:
    print("SK")
else:
    print("CY")
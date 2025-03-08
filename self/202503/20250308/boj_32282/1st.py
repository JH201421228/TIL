import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


X, Y, C = map(int, input().split())

dist = (X**2 + Y**2) ** .5

if not X and not Y:
    print(0)
elif dist < C:
    print(2)
elif dist % C:
    print(int(dist // C) + 1)
else:
    print(int(dist // C))
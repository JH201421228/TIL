import sys
sys.stdin = open('input.txt')

a, b, c, d, e, f = map(int, input().split())

if a*e - b*d: # a*e - b*d 값이 0이 아닌 경우
    x = (c*e - b*f)/(a*e - b*d)
    y = (c*d - a*f)/(b*d - a*e)
else: #a*e - b*d 값이 0인 경우(division error)
    x = 0
    y = 0
print(int(x), int(y))
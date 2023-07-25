a, b, c, d, e, f = map(int, input().split())

if a*e - b*d:
    x = (c*e - b*f)/(a*e - b*d)
    y = (c*d - a*f)/(b*d - a*e)
else:
    x = 0
    y = 0
print(int(x), int(y))

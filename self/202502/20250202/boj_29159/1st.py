import sys
sys.stdin = open("./input.txt")
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a%b

    return a


cordinates = [[0] * 2 for _ in range(2)]
for i in range(2):
    for _ in range(4):
        x, y = map(int, input().split())
        cordinates[i][0] += x
        cordinates[i][1] += y

    cordinates[i][0] /= 4
    cordinates[i][1] /= 4

a = int((cordinates[1][0] - cordinates[0][0]) * 16)
b = int((cordinates[1][1] - cordinates[0][1]) * 16)
c = int(a * cordinates[0][1] - b * cordinates[0][0])

ans = []

d1 = gcd(max(abs(a), abs(b)), min(abs(a), abs(b)))
d2 = gcd(max(abs(a), abs(c)), min(abs(a), abs(c)))

if d1 == abs(a):
    ans.append(b//a)
else:
    if a * b >= 0:
        ans.append(f"{abs(b)//d1}/{abs(a)//d1}")
    else:
        ans.append(f"-{abs(b) // d1}/{abs(a) // d1}")

if d2 == abs(a):
    ans.append(c//a)
else:
    if a * c >= 0:
        ans.append(f"{abs(c)//d2}/{abs(a)//d2}")
    else:
        ans.append(f"-{abs(c) // d2}/{abs(a) // d2}")

print(*ans)
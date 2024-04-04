import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


M = int(input())
lines = []
while True:
    a, b = map(int, input().split())
    if not a and not b:
        break
    if b <= 0:
        continue
    if a >= M:
        continue
    lines.append((a, b))
lines.sort(key=lambda x: (-x[0], x[1]))
# print(lines)

prea, preb = 0, 0
ans = 0
while lines:
    check = 0
    a, b = lines.pop()
    if not a and b >= preb:
        prea, preb = a, b
        ans = 1
    while lines:
        innera, innerb = lines.pop()
        if innera >= b:
            break
        if preb < innerb:
            preb = innerb
            check = 1
        

    if preb >= M:
        print(ans)
        exit(0)
print(0)


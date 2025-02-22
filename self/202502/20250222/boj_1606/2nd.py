import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def checker():
    if (x, y) == (xx, yy):
        print(shell_n)
        exit(0)

def mover(di, dj, i, j):
    global shell_n
    shell_n += 1
    return (di+i, dj+j)


down = (0, 1)
left = (-1, 1)
delta = [(-1, 0), (0, -1), (1, -1), (1, 0)]

x, y = map(int, input().split())

if not x and not y:
    print(1)
    exit(0)

shell = 0
shell_n = 1

if x * y > 0:
    shell = abs(x+y)
else:
    shell = max(abs(x), abs(y))

for i in range(1, shell):
    shell_n += 6*i

xx, yy = shell-1, 0

while True:
    checker()

    xx, yy = mover(down[0], down[1], xx, yy)
    checker()

    for _ in range(shell-1):
        xx, yy = mover(left[0], left[1], xx, yy)
        checker()

    for dx, dy in delta:
        for _ in range(shell):
            xx, yy = mover(dx, dy, xx, yy)
            checker()

    for _ in range(shell-1):
        xx, yy = mover(down[0], down[1], xx, yy)
        checker()
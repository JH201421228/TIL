import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def checker():
    if (x, y) == (xx, yy):
        print(n)
        exit(0)

def mover(di, dj, i, j):
    global n
    n += 1
    return (di+i, dj+j)



down = (0, 1)
left = (-1, 1)
delta = [(-1, 0), (0, -1), (1, -1), (1, 0)]

x, y = map(int, input().split())
xx, yy = 0, 0
n = 1
idx = 0
checker()

while True:
    for _ in range(idx+1):
        dx, dy = down
        xx, yy = mover(dx, dy, xx, yy)

        checker()

    for _ in range(idx):
        dx, dy = left
        xx, yy = mover(dx, dy, xx, yy)

        checker()

    for dx, dy in delta:
        for _ in range(idx+1):
            xx, yy = mover(dx, dy, xx, yy)

            checker()

    idx += 1
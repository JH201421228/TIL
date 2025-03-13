import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

if N == 1:
    print(1)
    exit(0)
elif not N % 2 or not N % 5:
    print(-1)
    exit(0)

rest = 1
acc = 1
cnt = 1

checker = [0] * 1_000_001

while True:
    rest = (rest * 10) % N
    acc = (acc + rest) % N

    cnt += 1

    if not acc:
        print(cnt)
        break

    if not rest:
        print(-1)
        break


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    a, b, d = map(int, input().split())

    if not a and not b and not d: exit(0)

    ans = []
    i = 1
    while True:
        if not (d-b*i) % (a-b):
            x = (d-b*i) // (a-b)
            y = i-x
            if x >= 0 and y >= 0: ans.append((a*x+b*y, x, y))

        if not (d+b*i) % (a+b):
            x = (d+b*i) // (a+b)
            y = i-x
            if x >= 0 and y >= 0: ans.append((a * x + b * y, x, y))

        if not (-d+b*i) % (a+b):
            x = (-d+b*i) // (a+b)
            y = i-x
            if x >= 0 and y >= 0: ans.append((a * x + b * y, x, y))

        if ans:
            ans.sort()
            break

        i += 1

    return ans[0][1], ans[0][2]


if __name__ == "__main__":
    while True:
        print(*solve())
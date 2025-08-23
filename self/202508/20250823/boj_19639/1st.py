import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    X, Y, M = map(int, input().split())

    enemies = [int(input()) for _ in range(X)]
    recoveries = [int(input()) for _ in range(Y)]

    if M + sum(recoveries) <= sum(enemies):
        print(0)
        return

    cur = M

    while enemies and recoveries:
        if cur > enemies[-1]:
            cur -= enemies.pop()
            print(-X)
            X -= 1
        else:
            while cur <= enemies[-1]:
                cur += recoveries.pop()
                print(Y)
                Y -= 1

    while X:
        print(-X)
        X -= 1

    while Y:
        print(Y)
        Y -= 1

    return


if __name__ == "__main__":
    solve()
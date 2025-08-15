import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def layer(n):

    return int((n-1)**.5)


def solve():
    A, B = map(int, input().split())
    A, B = min(A, B), max(A, B)

    step = [(A, A)]
    cnt = 0

    if A == B:
        print(0)
        return

    while True:
        if layer(step[-1][0]) == layer(B): break

        cnt += 1
        cur = step[-1][0]
        if (cur+layer(cur)) % 2:
            add = (layer(cur)+1)*2
            step.append((step[-1][0]+add, step[-1][1]+add))
        else:
            step.append((step[-1][0]-1, step[-1][1]+1))

    if B >= step[-1][0] and B <= step[-1][1]:
        if (B+layer(B)) % 2:
            print(cnt+1)
        else:
            print(cnt)
    else:
        if B < step[-1][0]:
            print(cnt + step[-1][0] - B)
        else:
            print(cnt + B - step[-1][1])

    return


if __name__ == "__main__":
    solve()
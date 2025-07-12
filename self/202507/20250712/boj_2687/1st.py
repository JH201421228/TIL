import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def init():
    for _ in range(int(input())):
        solve()

    return


def solve():
    B = int(input())
    data = ''

    while len(data) != 2*B:
        data += input().rstrip()

    idx = 0
    res = ''
    while idx < B:
        d = data[idx*2:idx*2+2]
        integer = int(d, 16)

        if integer >= 128:
            res += data[idx*2+2:idx*2+4]*(integer-128+3)
            idx += 2
        else:
            res += data[idx*2+2:idx*2+2+2*(integer+1)]
            idx += integer+2

    print(len(res)//2)
    idx = 0
    while idx < len(res):
        print(res[idx:idx+80])
        idx += 80

    return


if __name__ == "__main__":
    init()
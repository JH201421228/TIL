import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def solve():
    materials = [tuple(map(int, input().split())) for _ in range(int(input()))]

    ans = 0

    x, y = materials.pop()

    while materials:
        nx, ny = materials.pop()
        ans += (x*ny + y*nx)

        x, y = x+nx, y+ny

    return ans


if __name__ == "__main__":

    print(solve())
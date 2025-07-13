import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dotting(start_i, start_j, height, direction, canvas):
    canvas[start_i][start_j] = '*'
    for idx in range(start_j - height + 1, start_j + height): canvas[start_i + (height-1) * direction][idx] = '*'
    ni, nj = start_i + (height-1) * direction - direction, start_j

    sj, ej = start_j-1, start_j+1
    for i in range(start_i + direction, start_i + (height-1) * direction, direction):
        canvas[i][sj], canvas[i][ej] = '*', '*'
        sj -= 1
        ej += 1

    return canvas, ni, nj


def solve():
    N = int(input())
    res = [[' '] * (2**(N+1) - 3) for _ in range(2**N - 1)]

    si, sj = (2**N+ - 1) - (2**N - 1) ** (N % 2), (2**(N+1) - 3) // 2
    for i in range(N, 0, -1):
        res, si, sj = dotting(si, sj, 2**i - 1, 2*(i % 2) - 1, res)

    for line in res:
        print(''.join(line).rstrip())

    return


if __name__ == "__main__":
    solve()
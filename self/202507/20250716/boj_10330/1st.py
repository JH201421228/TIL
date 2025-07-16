import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def target_list(target, code):
    for n in code[1:]: target += str(1 - int(target[-1])) * n
    return list(map(int, target))

def solve(initial, target, N):
    res = 0
    i, j = 0, 0

    while True:
        if i == N-1 and j == N-1:
            break

        while True:
            if initial[i] == 1 and target[j] == 1:
                res += abs(i-j)
                i = min(i+1, N-1)
                j = min(j+1, N-1)
                break
            if initial[i] == 0: i = min(i+1, N-1)
            if target[j] == 0: j = min(j+1, N-1)

            if i == N - 1 and j == N - 1:
                break

    return res

def init():
    N, M = map(int, input().split())

    initial = list(map(int, input().split()))
    code = list(map(int, input().split()))

    initial_sum = sum(initial)

    ans = []

    if initial_sum == sum(code[::2]):
        target = target_list('1' * code[0], code)
        ans.append(solve(initial, target, N))


    if initial_sum == sum(code[1::2]):
        target = target_list('0' * code[0], code)
        ans.append(solve(initial, target, N))

    print(min(ans))

    return


if __name__ == "__main__":
    init()
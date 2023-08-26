import sys
sys.stdin = open('input.txt')

def what_the(N, start, end):
    if N == 1:
        for idx in range(start, end + 1):
            ans_list[idx] = 1
        return

    third = (end - start + 1) // 3

    what_the(N - 1, start, start + third - 1)
    what_the(N - 1, start + third, start + 2 * third - 1)
    what_the(N - 1, start + 2 * third, end)

while True:
    try:
        n = int(input())
        ans_list = [0] * (3**n)
        what_the(n, 0, len(ans_list) - 1)
        print(' '.join(map(str, ans_list)))
    except EOFError:
        break

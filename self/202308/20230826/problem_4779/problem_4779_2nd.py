import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(15000)

def what_the(N, length):
    if N == 0:
        for char in ans_list:
            if not char:
                print(' ', end='')
            else:
                print(char, end='')
        print()
        return

    for idx in range(length):
        if (idx // (3**(N-1))) % 3 == 1:
            ans_list[idx] = 0
    what_the(N-1, length)


while True:
    try:
        n = int(input())
        ans_list = ['-'] * (3**n)
        # print(ans_list)
        what_the(n, len(ans_list))
    except EOFError:
        break
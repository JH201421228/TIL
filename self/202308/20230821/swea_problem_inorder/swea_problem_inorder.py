import sys
sys.stdin = open('input.txt')


def inorder(N):
    if not N:
        return
    inorder(left[N])
    ans.append(char_list[N])
    inorder(right[N])


for test in range(10):
    N = int(input())
    char_list = [' ']
    for _ in range(N):
        char = list(input().split())
        char_list.append(char[1])

    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(2, N+1):
        if not i % 2:
            left[(i-1) // 2 + 1] = i
        else:
            right[(i-1) // 2] = i
    ans = []
    inorder(1)
    ans_word = ''.join(ans)
    print(f'#{test+1} {ans_word}')


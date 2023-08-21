import sys
sys.stdin = open('input.txt')


def inorder(N):
    if not N:
        return
    inorder(left[N])
    ans.append(N)
    inorder(right[N])


Test = int(input())
for test in range(Test):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(2, N+1):
        if not i % 2:
            left[(i - 1) // 2 + 1] = i
        else:
            right[(i - 1) // 2] = i
    ans = [0]
    inorder(1)
    print(f'#{test + 1} {ans.index(1)} {ans.index(N//2)}')

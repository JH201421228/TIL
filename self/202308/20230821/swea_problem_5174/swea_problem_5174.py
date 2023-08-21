import sys
sys.stdin = open('input.txt')


def preorder(N):
    if not N:
        return
    ans.append(N)
    preorder(left[N])
    preorder(right[N])


Test = int(input())
for test in range(Test):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    for i in range(E):
        if not left[info[2*i]]:
            left[info[2 * i]] = info[2*i+1]
        else:
            right[info[2*i]] = info[2*i+1]
    ans = []
    preorder(N)
    print(f'#{test+1} {len(ans)}')

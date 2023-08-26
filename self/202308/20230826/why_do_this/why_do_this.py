import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    a = []
    result = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            b = str(data[i] * data[j])
            a.append(b)
    print(a)

    for i in a:
        tmp = 0
        for j in range(len(i) - 1):
            if i[j] <= i[j + 1]:
                tmp = int(i)
            else:
                tmp = 0
                break
        if tmp != 0:
            result = tmp

    if result == 0:
        result = -1

    print(f'#{tc} {result}')
import sys
sys.stdin = open('input.txt')


def what_the(N, start):
    if len(arr) == N:
        print(arr)
        ans.append(sum(arr))
        return

    for i in range(start, N):
        for j in range(N):
            if j not in y_index_info:
                y_index_info.append(j)
                arr.append(matrix[i][j])
                what_the(N, i+1)
                y_index_info.pop()
                arr.pop()




Test_Case = int(input())

for test_case in range(Test_Case):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    arr = []
    y_index_info = []
    ans = []
    what_the(N, 0)
    print(min(ans))
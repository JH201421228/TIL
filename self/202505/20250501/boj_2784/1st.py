import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def checker(arr):
    temp = []
    for j in range(3):
        c = ''
        for i in range(3):
            c += arr[i][j]
        temp.append(c)

    cmp = []
    for idx in range(6):
        if not V[idx]: cmp.append(words[idx])

    temp.sort()
    cmp.sort()

    if temp == cmp: return True
    else: return False


def solve(n, temp):

    if n == 3:
        if checker(temp):
            for inner in temp:
                print(inner)
            exit(0)
        return

    for idx in range(6):
        if V[idx]: continue
        temp.append(words[idx])
        V[idx] = 1
        solve(n+1, temp)
        V[idx] = 0
        temp.pop()

    return


words = [input().rstrip() for _ in range(6)]
V = [0] * 6
temp = []

solve(0, temp)
print(0)
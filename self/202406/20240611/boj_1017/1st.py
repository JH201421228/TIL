import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1_000)


def Bi(n, e):
    for i in range(M):
        x = B[i]
        if x == e:
            continue
        if V[x]:
            continue
        if not seive[n+x]:
            continue
        V[x] = 1

        if not C[x] or Bi(C[x], e):
            C[x] = n
            return True

    return False


seive = [True] * 2_001
for i in range(2, int(2_000**0.5)+1):
    if seive[i]:
        j = i**2
        while j <= 2000:
            seive[j] = False
            j += i

N = int(input())
temp = list(map(int, input().split()))
A, B = [], []
first = temp.pop(0)

if first % 2:
    while temp:
        out = temp.pop(0)
        if out % 2:
            A.append(out)
        else:
            B.append(out)
else:
    while temp:
        out = temp.pop(0)
        if out % 2:
            B.append(out)
        else:
            A.append(out)

N, M = len(A), len(B)
if N+1 == M:
    ans = []
    for i in range(M):
        if seive[first+B[i]]:
            C = [0] * 1_001
            C[B[i]] = first
            for v in A:
                V = [0] * 1_001
                Bi(v, B[i])
            check = 0
            for c in B:
                if C[c]:
                    check += 1
            if check == M:
                ans.append(B[i])
    if ans:
        ans.sort()
        print(*ans)
    else:
        print(-1)
else:
    print(-1)
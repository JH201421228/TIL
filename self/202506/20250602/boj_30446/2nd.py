import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)  # DFS 깊이 제한 해제

n = int(sys.stdin.readline())
posn = len(str(n))
endn = (posn + 1) // 2
ans = 0
fin = False
res = ['0'] * posn

def dfs(idx):
    global ans, fin
    if fin:
        return
    if idx == endn:
        num = int(''.join(res))
        if num <= n:
            ans += 1
        else:
            fin = True
        return

    if idx == 0:
        for i in range(1, 10):
            res[idx] = res[posn - idx - 1] = str(i)
            dfs(idx + 1)
            if fin:
                return
    else:
        for i in range(10):
            res[idx] = res[posn - idx - 1] = str(i)
            dfs(idx + 1)
            if fin:
                return

# 먼저 자리수 작은 회문수는 공식으로 더하기
for i in range(1, posn):
    tmp = 9
    endt = (i + 1) // 2
    for j in range(1, endt):
        tmp *= 10
    ans += tmp

# 현재 자리수 회문수는 DFS로 생성
dfs(0)

# 결과 출력
print(ans)

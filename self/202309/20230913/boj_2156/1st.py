import sys
sys.stdin = open('input.txt')

n = int(input())
wine = [int(input()) for _ in range(n)]
let_s_go = [[0]*3 for _ in range(n)]
let_s_go[0][1] = wine[0]
for i in range(1, n):
    let_s_go[i][0] = max(let_s_go[i-1])
    let_s_go[i][1] = let_s_go[i-1][0] + wine[i]
    let_s_go[i][2] = let_s_go[i-1][1] + wine[i]
print(max(let_s_go[-1]))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
D = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            u = (D[i][0]-D[j][0], D[i][1]-D[j][1])
            v = (D[i][0]-D[k][0], D[i][1]-D[k][1])

            ans = max(ans, abs(u[0]*v[1]-u[1]*v[0])/2)

print(ans)
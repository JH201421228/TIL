

n, m = map(int, input().split())
li = []

for i in range(1,n+1):
    li.append(i)

for _ in range(m):
    c = 0
    d = 0
    a, b = map(int, input().split())
    
    c = li[a-1]
    d = li[b-1]
    li[a-1] = d
    li[b-1] = c
    
for i in range(n):
    print(li[i], end=' ')
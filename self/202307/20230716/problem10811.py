n, m = map(int, input().split())
# 바구니 개수 n, 시행 횟수 m

li = []

for i in range(1, n+1):
    li.append(i)
    # 숫자를 채움
    
for _ in range(m):
    temp = []
    a, b = map(int, input().split())
    temp = li[a-1: b]
    temp.reverse()
    li[a-1: b] = temp

for _ in range(n):
    
    print(li[_], end=' ')

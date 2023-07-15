t = int(input())

for _ in range(t):
    
    n, m = map(int, input().split())
    mat = [list(map(int,input().split())) for i in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    tx = [1,1,-1,-1]
    ty = [1,-1,1,-1]
    
    total = 0
    ans = 0
    
    for i in range(n):
        
        for j in range(n):
            
            su1 = mat[i][j]
            su2 = mat[i][j]
            
            for k in range(4):
                
                for l in range(1,m):
                    
                    a = i + dx[k]*l
                    b = j + dy[k]*l
                    
                    c = i + tx[k]*l
                    d = j + ty[k]*l

                    if 0 <= a < n and 0 <= b < n:
                        
                        su1 += mat[a][b]
                        
                    if 0 <= c < n and 0 <= d < n:
                        
                        su2 += mat[c][d]

            total = max(su1, su2)
            if total > ans:
                ans = total



    print(f'#{_+1} {ans}')     
            
                
                 
    
    
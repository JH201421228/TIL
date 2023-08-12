

t = int(input()) # 테스트 케이스 개수

for _ in range(t): # 테스트 개수 만큼 반복
    
    n, m = map(int,input().split()) #각각 배열 크기, 세기
    mat = [list(map(int,input().split())) for i in range(n)]
    # 행렬 입력 받음
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    tx = [-1,-1,1,1]
    ty = [1,-1,1,-1]
    # 각 방향 벡터 정의
    
    total = 0
    ans = 0
    
    for i in range(n):
        
        for j in range(n): # 입력받은 행렬 요소 개수만큼 반복
            ca1 = mat[i][j]
            ca2 = mat[i][j]
            #분사할 위치
            
            for k in range(4): # 4 방향 분사
                
                for l in range(1,m): # 분사 세기
                    a = i + dx[k]*l
                    b = j + dy[k]*l
                    c = i + tx[k]*l
                    d = j + ty[k]*l
                    
                    # 각 방향 좌표 설정
                    
                    if 0 <= a < n and 0 <= b < n: #행렬 좌표 안에 존재할 시 실행
                        ca1 += mat[a][b]
                        
                    if 0 <= c < n and 0 <= d < n:
                        ca2 += mat[c][d]
                        
            total = max(ca1, ca2)
            if total > ans:
                ans = total # 최대값 갱신
    print(f'#{_+1} {ans}')
                
            
            
            
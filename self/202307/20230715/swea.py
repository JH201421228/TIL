

def row_check(a):
    
    for i in range(9):
        
        if len(set(a[i])) == len(a[i]):
            
            continue
        
        else:
            
            return 0
    
    return 1

def col_check(a):
    
    for i in range(9):
        
        li = []
        
        for j in range(9):
        
            li.append(a[j][i])
        
        if len(li) == len(set(li)):
            
            continue
        
        else:
            
            return 0
    
    return 1
    
def rec_check(a):
    
    for i in range(3):
        
        li1 = []
            
        li2 = []
            
        li3 = []
            
        for j in range(3*i, 3*(i+1)):
        
            for k in range(0, 3):
                
                li1.append(a[j][k])
            
            for l in range(3, 6):
                
                li2.append(a[j][l])
            
            for m in range(6, 9):
                
                li3.append(a[j][m])
                
        if len(set(li1))==len(li1) and len(set(li2))==len(li2) and len(set(li3))==len(li3):
           
            continue
            
        else:
                
            return 0
        
    return 1
        
        
n = int(input())

mat = [list(map(int, input().split(' '))) for _ in range(9*n)]

for i in range(n):
    
    print(f'#{i+1} {row_check(mat[i*9:9*(i+1)]) * col_check(mat[i*9:9*(i+1)]) * rec_check(mat[i*9:9*(i+1)])}')


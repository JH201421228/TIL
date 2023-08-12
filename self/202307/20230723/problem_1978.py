N = int(input())
M = list(map(int, input().split()))
ans_list = []

for i in range(N):
    
    if M[i] == 1:
        continue
    
    elif M[i] == 2:
        ans_list.append(M[i])
    
    else:
        checker = []
        for j in range(2, M[i]):
            if M[i] % j == 0:
                checker.append(j)
                
        if len(checker) == 0:
            ans_list.append(M[i])
            

        
print(len(ans_list))
        
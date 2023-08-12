M = int(input())
N = int(input())

num_list = []

for i in range(M, N + 1):
    if i == 1:
        continue
    
    elif i == 2:
        num_list.append(i)
        continue
    
    else:
        checker = []
        
        for j in range(2, i):
            if i % j == 0:
                checker.append(j)
            
        if len(checker) == 0:
            num_list.append(i)
                
if len(num_list) == 0:
    print(-1)

else:
    print(sum(num_list))
    print(num_list[0])
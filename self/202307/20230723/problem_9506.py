while True:
    ans_list = []
    N = int(input())
    
    if N == -1:
        break
    
    for i in range(1, N):
        if N % i ==0:
            ans_list.append(i)
            
    if N == sum(ans_list):
        print(f'{N} = ',end = '')
        for i in ans_list:
            if i == ans_list[len(ans_list) - 1]:
                print(i)
            else:
                print(f'{i} + ', end = '')
    else:
        print(f'{N} is NOT perfect.')        
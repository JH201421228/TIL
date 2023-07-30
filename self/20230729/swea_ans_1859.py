N = int(input()) #수정중

# input_list = [2, 4, 6, 8, 10, 6, 7, 5, 6]



for j in range(N):
    days = int(input())
    input_list = list(map(int, input().split()))
    total = 0
    while True:
        max_val = max(input_list)
        max_index = input_list.index(max_val)
        

        for i in input_list[:max_index]:
            total += (max_val - i)

        input_list = input_list[max_index + 1:]
        
        # print(f'max_val: {max_val}')
        # print(f'max_index: {max_index}')
    
        
        if not input_list:
            print(f'#{j + 1} {total}')
            break

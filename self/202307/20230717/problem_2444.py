

star_num = int(input())

for i in range(star_num):
    
    for j in range(star_num - i - 1):
        print(' ', end = '')
    
    for j in range(2 * i + 1):
        print('*', end = '')
        
    print()
    
    
for i in range(star_num - 1):
    
    for j in range(i + 1):
        print(' ', end = '')
        
    for j in range(2 * (star_num - i - 1) - 1):
        print('*', end = '')
        
    print()
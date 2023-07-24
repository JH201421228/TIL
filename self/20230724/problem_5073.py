tri_len = []

while True:
    tri_len = list(map(int, input().split()))
    
    if tri_len.count(0) == 3:
        break
    
    elif 2 * max(tri_len) >= sum(tri_len):
        print('Invalid')
        
    elif len(set(tri_len)) == 1:
        print('Equilateral')
        
    elif len(set(tri_len)) == 2:
        print('Isosceles')
        
    else:
        print('Scalene')
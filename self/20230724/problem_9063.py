T = int(input())

point_list = []
x_cordinate = []
y_cordinate = []

for i in range(T):
    point_list.append(list(map(int, input().split())))
    
if T == 1:
    print(0)
    
else:
    for i in point_list:
        x_cordinate.append(i[0])
        y_cordinate.append(i[1])
        
    ans = (max(x_cordinate) - min(x_cordinate)) * (max(y_cordinate) - min(y_cordinate))
    print(ans)
        

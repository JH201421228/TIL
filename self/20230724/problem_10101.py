angle_list = []

for i in range(3):
    angle_list.append(int(input()))
    
if sum(angle_list) != 180:
    print('Error')
    
elif angle_list[0] == 60 and angle_list[1] == 60:
    print('Equilateral')
    
elif angle_list[0] == angle_list[1] or angle_list[0] == angle_list[2] or angle_list[2] == angle_list[1]:
    print('Isosceles')
    
else:
    print('Scalene')
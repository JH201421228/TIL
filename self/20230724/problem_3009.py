point1 = list(map(int, input().split()))
point2 = list(map(int, input().split()))
point3 = list(map(int, input().split()))
point4 = []

x_cordinate = [point1[0], point2[0], point3[0]]
y_cordinate = [point1[1], point2[1], point3[1]]

for i in range(3):
    if x_cordinate.count(x_cordinate[i]) == 1:
        point4.append(x_cordinate[i])
        
for i in range(3):
    if y_cordinate.count(y_cordinate[i]) == 1:
        point4.append(y_cordinate[i])
        
   
print(*point4)
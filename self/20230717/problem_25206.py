
nums = 20

total = 0
subject = 0

for _ in range(20):
    information = str(int())
    
    if information[-1] == 'P':
        pass
    
    elif information[-1] == 'F':
        subject += int(information[-5])
        
    elif information[-2] == 'A' and information[-1] == '+':
        total += int(information[-6]) * 4.5
        subject += int(information[-6])
# print(input()[-6])
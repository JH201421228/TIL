N = int(input())
num_list = []
num = N

for i in range(2, N + 1):
    if N == 1:
        print()
        break
    else:
        while num % i == 0:
            num_list.append(i)
            num = num // i
            
for i in num_list:
    print(i)
num1, num2 = map(int, input().split())

max_num = max(num1, num2)
min_num = min(num1, num2)

for num in range(1, min_num+1):
    if (max_num * num) % min_num == 0:
        print(max_num * num)
        break
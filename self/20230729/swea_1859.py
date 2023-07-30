N = int(input())

for i in range(N):
    days = int(input())
    price_list = list(map(int, input().split()))
    total = 0
        
    for j in range(len(price_list) - 1):
        if price_list[j] < max(price_list[j+1:]):
            total += max(price_list[j+1:]) - price_list[j]
            print(price_list)
    print(f'#{i+1} {total}')
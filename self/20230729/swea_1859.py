N = int(input())
# 테스트 횟수 입력받음

for i in range(N):
    days = int(input())
    price_list = list(map(int, input().split()))
    total = 0
    # 입력값을 list에 저장

    for j in range(len(price_list) - 1):
        if price_list[j] < max(price_list[j+1:]):
            total += max(price_list[j+1:]) - price_list[j]
            print(price_list)
    # 현재 값이 미래의 미래의 어떤 값보다 작으면, 그 차이를 total에 더함
    
    print(f'#{i+1} {total}')
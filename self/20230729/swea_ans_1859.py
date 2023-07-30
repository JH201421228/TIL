N = int(input())


for j in range(N):
    days = int(input())
    input_list = list(map(int, input().split()))
    total = 0
    # 가격 데이터를 list에 입력받음

    while True:
        max_val = max(input_list)
        max_index = input_list.index(max_val)
        # 현재 리스트가 가지고 있는 최댓값과 그 인덱스를 저장

        for i in input_list[:max_index]:
            total += (max_val - i)
        # 인덱스 0부터 최댓값이 있는 구간까지의 모든 값과, 최댓값간의 차이를 total에 합산

        input_list = input_list[max_index + 1:]
        # 최대값 이전의 값은 잘라내고 남은 리스트만 저장
        
        if not input_list:
            print(f'#{j + 1} {total}')
            break
        # 상기 과정을 반복하며, 리스트에 값이 없어지면 total의 값을 출력
import sys
from collections import deque
sys.stdin = open('input.txt')

Test = int(input())

for test in range(Test):
    maker_size, total_pizza = map(int, input().split()) # 피자를 구울 화덕의 크기와 총 피자 개수를 각각 받습니다.
    pizza_maker = deque([]) # 피자를 구울 화덕입니다.
    total_pizza_que = deque(list(map(int, input().split()))) # 모든 피자의 치즈 정보를 받아옵니다.
    censored_pizza_que = deque([]) # 바로 위에서 받은 모든 피자의 치즈 정보를 인덱스와 함께 저장할 큐를 만듭니다.

    i = 1
    while total_pizza_que: # 받아온 피자의 정보가 담긴 큐가 빌때 까지 반복합니다.
        censored_pizza_que.append([total_pizza_que.popleft(), i]) # 피자의 치즈 정보와 몇번째 피자인지 리스트를 함께 저장합니다.
        i += 1

    for _ in range(maker_size): # 화덕에 피자를 미리 채워놓습니다.
        pizza_maker.append(censored_pizza_que.popleft()) # 화덕에 피자를 채우면서 피자정보와 인덱스가 든 큐는 팝해줍니다.

    while pizza_maker: # 화덕에 피자가 없어질때 까지 반복합니다.
        now_pizza = pizza_maker.popleft() # 현재 꺼낼 피자의 정보를 받습니다.
        now_pizza[0] = now_pizza[0]//2 # 현재 꺼낸 피자의 치즈를 반으로 줄입니다.
        if not now_pizza[0]: # 이때 피자의 치즈가 0이 되면
            if censored_pizza_que: # 새로운 피자를 넣기위해 censored_pizza_que에 남은 피자가 있는지 확인하고
                pizza_maker.append(censored_pizza_que.popleft()) # 더 넣을 피자가 있다면 넣어줍니다.
        else:
            pizza_maker.append(now_pizza) # 피자의 치즈가 0이 아니라면 화덕의 맨 끝에 다시 돌려 놓습니다.

    print(f'#{test + 1} {now_pizza[1]}') # 마지막 피자의 정보를 가지고 있는 now_pizza를 가지고와 몇번째 인덱스인지 출력합니다.
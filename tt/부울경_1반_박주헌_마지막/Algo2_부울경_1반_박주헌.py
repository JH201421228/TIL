

Test = int(input()) # 테스트를 진행할 횟수를 받아옵니다.
for test in range(Test): # 테스트 횟수만큼 반복합니다.
    N, M = map(int, input().split()) # 처음에 카드가 몇개인지, 김 싸피가 몇 번째로 카드를 가져갈지에 대한 정보를 받아옵니다.
    A_list = list(map(str, input().split())) # 처음 카드 리스트를 받아옵니다.
    B_que = [] # 큐로 쓰일 빈 리스트를 만듭니다.
    C_stack = [] # 스택으로 쓰일 빈 리스트를 만듭니다.
    bonus = 0 # 보너스 점수로 쓰일 변수를 선언합니다.
    for num in A_list: # A_list를 순회하겠습니다.
        if num.isdigit(): # 해당 값이 숫자라면
            input_num = int(num) + bonus # 정수형태로 변경후 보너스 값을 더해 새로운 변수에 할당하겠습니다.
            if input_num % 2: # 해당 변수가 홀수일 경우
                B_que.append(input_num) # 큐에 넣겠습니다.
            else: # 짝수일 경우
                C_stack.append(input_num) # 스택에 넣겠습니다.
        else: # 해당 값이 숫자형태가 아니라면
            bonus += 1 # 보너스 점수를 증가시킵니다.

    score_list = [] # 점수를 저장할 리스트를 만듭니다.
    for _ in range(M): # 김싸피의 순서가 될 때 까지 게임을 진행하겠습니다.
        score = 0 # 초기 점수를 선언합니다.
        if B_que: # 큐에 값이 있다면
            score += B_que.pop(0) # 큐의 가장 먼저 들어온 값을 스코어에 더해줍니다.
        if C_stack: # 스택에 값이 있다면
            score += C_stack.pop() # 스택에 가장 늦게 들어온 값을 스코어에 더해줍니다.
        score_list.append(score) # 점수를 리스트에 저장합니다.
    print(f'#{test+1} {score_list[-1]}') # 김싸피의 점수는 리스트 가장 마지막에 저장되어 있으므로 해당 형태로 출력해줍니다.
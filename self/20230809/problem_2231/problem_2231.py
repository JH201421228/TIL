import sys
sys.stdin = open('input.txt')

N = int(input())

ans = 0

for num in range(0, N+1): # 브루트 포스
    sum_num = num # 각 값을 더할 변수
    maybe_ans = num # 답인지 체크할 변수

    while True:
        if maybe_ans < 10: # 10보다 작은 값은 sum_num에 더하고 탈출
            sum_num += maybe_ans
            break
        else:
            sum_num += maybe_ans % 10 # 10으로 나눈 나머지를 더해줌
            maybe_ans //= 10 # 10으로 나눈 몫으로 갱신함

    if N == sum_num: # 조건이 맞는지 확인
        ans = num
        break
print(ans) # 답을 출력
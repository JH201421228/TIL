import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
card_list = list(map(int, input().split())) # 입력값 받음

max_val = 0 # 최대값 변수 선언

for i in range(N - 2): # 첫 번째 카드
    for j in range(i + 1, N - 1): # 두 번째 카드
        for k in range(j + 1, N): # 세 번째 카드
            sum_val = card_list[i] + card_list[j] + card_list[k] # 세 카드의 합
            if sum_val > max_val and sum_val <= M: # 세 카드의 합이 최댓값보다 크고, M 보다 작으면, 최대값을 교체
                max_val = sum_val

print(max_val)
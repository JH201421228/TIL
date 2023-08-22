import sys
sys.stdin = open('input.txt')


from itertools import combinations # 조합 내장 함수를 가져옵니다.(조합 - 유한 개의 원소에서 주어진 수 만큼의 원소들을 고르는 방법. 단 순서가 중요하지 않음.)

N, sum_val = map(int, input().split()) # 정수의 개수와 정수의 합을 받아옵니다.
numbers = list(map(int, input().split())) # 숫자들을 받아와 리스트에 저장합니다.
cnt = 0 # 부분수열의 개수를 저장할 변수를 선언합니다.
for i in range(1, N+1): # 사용할 수 있는 숫자의 개수만큼 반복합니다.
    ans_list = combinations(numbers, i) # numbers 리스트에서 i개의 원소를 갖는 조합을 찾아 리스트에 저장합니다.
    for ans in ans_list: # 조합이 담긴 리스트를 순회합니다.
        if sum(ans) == sum_val: # 조합의 합이 원하는 값과 같다면
            cnt += 1 # 카운트 합니다.
print(cnt)
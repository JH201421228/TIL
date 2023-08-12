import sys
from itertools import permutations # 순열 함수를 구현 못해서 내장 함수 썻읍니다...
# sys.stdin = open('input.txt')

n = int(input())
k = int(input())
input_list = []
ans_set = set() # 중복 제거를 위해 set 사용

for _ in range(n):
    input_list.append(input()) # 값 입력받음

for inner_str in list(permutations(input_list, k)): # 해당 리스트를 순회하면서...
    ans_set.add(int(''.join(inner_str))) # str로 저장된 숫자들을 join하고 정수형태로 바꿔서 set에 추가

print(len(ans_set)) # 세트에 들어있는 정수 개수 출력

import sys
from itertools import product
# sys.stdin = open('input.txt')

N, K_num = map(int, input().split())
num_list = list(map(str, input().split())) # 값 입력 받음

length = len(str(N)) # 근사해야 하는 정수의 자릿수
num_list.sort(reverse= True) # 내림차순 정렬

product_list = list(product(num_list, repeat= length)) # 상기 자릿수와 같은 자릿수를 가진 정수 생성

for inner_str in product_list:
    if int(''.join(inner_str)) <= N: # str 형태를 int로 변환 후 N과 대소비교
        print(int(''.join(inner_str))) # 답을 찾으면 출력
        break
else:
    print(num_list[0]*(length-1)) # for문을 다 돌고도 break를 못 건 경우 한자리 적은 가장 큰 정수를 출력







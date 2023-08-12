# 기차 사이의 파리
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    distance, A_speed, B_speed, fly_speed = map(int, input().split())
    ans = fly_speed*(distance/(A_speed+B_speed))
    print(f'#{test_case + 1} {ans}')
# 원 안의 점
import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    Radius = int(input())
    cnt = 0
    for x in range(-Radius, Radius+1):
        for y in range(-Radius, Radius+1):
            if (x**2 + y**2) <= Radius**2:
                cnt += 1
    print(f'#{test_case + 1} {cnt}')
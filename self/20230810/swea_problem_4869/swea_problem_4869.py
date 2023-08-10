import sys
sys.stdin = open('input.txt')


def paper_craft(num):
    result = [0] * (num//10 + 1) # 함수 내부에 리스트 생성
    if num % 10:
        return False
    else:
        result[1] = 1
        result[2] = 3
        for i in range(3, num//10 + 1):
            result[i] = result[i-1] + 2 * result[i-2] # 종이접기 문제의 점화식

        return result


Test_Case = int(input())

for test_case in range(Test_Case):
    num = int(input())
    print(f'#{test_case + 1} {paper_craft(num)[-1]}')
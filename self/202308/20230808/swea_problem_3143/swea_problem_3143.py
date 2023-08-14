import sys
sys.stdin = open('input.txt')

Test_Case = int(input())

for test_case in range(Test_Case):
    str1, str2 = map(str, input().split())
    # str1 에 전체 문자열, str2에 찿을 문자열 저장

    out_str = str1.split(str2)
    # print(out_str) ## 참고용


    ans1 = len(out_str) - 1 # str2가 str1에 몇개 들어있는가?
    ans2 = 0

    for inner_str in out_str: # out_str에 남아있는 문자 개수 = ans2
        ans2 += len(inner_str)

    ans = ans1 + ans2
    print(f'#{test_case + 1} {ans}')
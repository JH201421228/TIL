import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    student_num, report_num = map(int, input().split())
    report_student = list(map(int, input().split()))
    all_student = [i for i in range(1, student_num+1)]
    print(f'#{test+1}', end=' ')
    print(*(set(all_student)-set(report_student)))
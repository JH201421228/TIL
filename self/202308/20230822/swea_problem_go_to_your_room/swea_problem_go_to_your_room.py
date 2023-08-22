import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    students_num = int(input())
    corridor = [0] * 201
    for _ in range(students_num):
        p1, p2 = map(int, input().split())
        if p2 >= p1:
            for i in range((p1-1)//2, (p2-1)//2 + 1):
                corridor[i] += 1
        else:
            for i in range((p2-1)//2, (p1-1)//2 + 1):
                corridor[i] += 1
    # print(corridor)
    print(f'#{test+1} {max(corridor)})')
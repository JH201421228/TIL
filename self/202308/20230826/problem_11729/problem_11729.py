import sys
sys.stdin = open('input.txt')


# 1. 옮길 수 있는 가장 큰 숫자를 옮기고
# 2. 직전 옮겼던 값은 옮기지 않고
# 3. 빈 스택이나 본인보다 큰 값 위에만 올라간다.

def tower(num): # num 은 직전에 옮긴 숫자
    global cnt
    cnt += 1

    if not stack1 and (not stack2 or not stack3):
        print(ans_list)
        exit(0)






N = int(input())
stack1 = [i for i in range(1, N+1)]
stack2 = []
stack3 = []
ans_list = []
cnt = 0

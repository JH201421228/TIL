import sys
sys.stdin = open('input.txt')

def divider(start, end):
    if start == end: # 재귀함수를 돌며 start와 end 값이 같아지면 해당 값을 반환(해당 값은 numbers의 인덱스임)
        return start
    left = divider(start, (start+end)//2) # 해당 함수를 탈출할때 까지 반복
    right = divider((start+end)//2+1, end) # 상기 재귀함수를 탈출하면 해당 재귀함수를 탈출할때 까지 반복
    return the_game(left, right) # 상기

def the_game(left, right):
    if numbers[left] == numbers[right]: # 1은 가위, 2는 바위, 3은 보를 나타낸다.
        return left

    elif numbers[left] == 1:
        if numbers[right] == 2:
            return right
        elif numbers[right] == 3:
            return left

    elif numbers[left] == 2:
        if numbers[right] == 1:
            return left
        elif numbers[right] == 3:
            return right

    elif numbers[left] == 3:
        if numbers[right] == 1:
            return right
        elif numbers[right] == 2:
            return left


Test = int(input())
for test in range(Test):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{test + 1} {divider(0, N-1) + 1}')
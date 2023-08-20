import sys
sys.stdin = open('input.txt')

Test = int(input())

for test in range(Test):
    correct = list(map(int, input())) # 현재 코드를 받아옵니다.
    wrong = [0] * len(correct) # 잘못된 코드를 만들어 놓습니다.
    cnt = 0 # 몇번 수정했는지 나타낼 변수를 선언합니다.
    for i in range(len(correct)): # 코드의 길이만큼 순회하면서
        if correct[i] != wrong[i]: # 맞는 코드와 잘못된 코드의 값이 다른 지점에서
            now = wrong[i] # 해당 지점 값을 저장하고
            for j in range(i, len(correct)): # 해당 지점 이후부터 끝까지의 값을 바꿉니다.
                wrong[j] = 1 - now # 이런식으로요
            cnt += 1 # 그리고 카운트를 해주면 되겠죠?
    print(f'#{test+1} {cnt}')
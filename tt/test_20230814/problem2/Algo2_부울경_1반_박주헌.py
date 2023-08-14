import sys
sys.stdin = open('input.txt')
########################################

def bracket_checker(strs): # 괄호가 제대로 되어 있는 상태인지 검사하는 함수를 만듭니다.
    if type(strs[0]) == int or type(strs[-1]) == int: # 만약 맨 앞 혹은 맨 뒤에 저장된 값이 정수형이라면 False를 반환합니다.
        return False

    stack1 = []
    stack2 = [] # 스택으로 쓸 리스트를 2개 만듭니다.
    for something in strs: # 반복문을 돌며 괄호들만 stack1에 저장합니다.
        if something == '(' or something == ')' or something == '{' or something == '}':
            stack1.append(something)

    while stack1: # stack1이 변수를 가지고 있는 동안
        if stack1 and stack2 and ((stack1[-1] == '(' and stack2[-1] == ')') or (stack1[-1] == '{' and stack2[-1] == '}')): # stack1과 stack2가 값을 가지고 있고, 각 스택의 마지막에 저장된 괄호가 짝을 이루면
            stack1.pop()
            stack2.pop() # 각 스택의 마지막 괄호를 팝해서 없애줍니다.
        else:
            stack2.append(stack1.pop()) # 만약 stack2가 비어있거나, 각 스택의 마지막에 저장된 괄호가 짝이 맞지 않다면, stack1의 마지막 괄호를 stack2로 옮겨줍니다.

    if stack2: # 상기 과정이 끝난 상태에서 stack2에 괄호가 남아있다면 False를 반환합니다.
        return False
    else: # stack2에 괄호가 남아있지 않다면, 모든 괄호가 짝이 맞는 상황이므로 True를 반환합니다.
        return True


def bracket_math(problems): # 괄호 내부를 주어진 규칙에 따라 계산하는 함수를 만듭니다.
    stack1 = []
    stack2 = [] # 두개의 스택을 만듭니다.
    stack1.extend(problems) # stack1에는 받은 변수를 전부 넣어줍니다.
    total = 0 # 계산 결과가 될 변수를 선언합니다.
    while stack1:
        if stack1[-1] == ')' or stack1[-1] == '}': # 스택1의 마지막 값이 닫는 괄호라면 스택2로 옮깁니다.
            stack2.append(stack1.pop())
        elif type(stack1[-1]) == int: # 스택1의 마지막 값이 정수라면 스택2로 옮깁니다.
            stack2.append(stack1.pop())
        elif stack1[-1] == '(': # 스택1에 여는 괄호가 나오면,
            while stack2[-1] != ')': # 스택2에 닫는 괄호가 나올때 까지,
                total += stack2.pop() # 해당 연산을 수행합니다.
            stack1.pop()
            stack2.pop() # 이후 각 스택 마지막에 저장된 괄호를 없애주기 위해 팝을 합니다.
        elif stack1[-1] == '{':
            while stack2[-1] != '}':
                if total: # 만약 total 값이 0인 경우 곱하기 연산을 수행하면 0이 되므로 해당 과정을 추가합니다.
                    total *= stack2.pop()
                else:
                    total = stack2.pop()
            stack1.pop()
            stack2.pop()
    return total # 결과를 반환합니다.



Test_Case = int(input())
for test_case in range(Test_Case):
    input_str = input() # 인풋을 스트링 형태로 받습니다.
    problems = []
    for str_int in input_str: # 스트링 형태로 저장된 변수들을 정수는 정수로, 스트링은 스트링으로 분리하여 리스트에 저장합니다.
        try:
            problems.append(int(str_int))
        except:
            problems.append(str_int)

    if bracket_checker(problems): # 괄호 검사를 통과하면
        print(f'#{test_case+1} {bracket_math(problems)}') # 괄호 계산을 하여 출력합니다.
    else:
        print(f'#{test_case+1} -1') # 괄호 검사를 통과하지 못하면 이처럼 출력합니다.
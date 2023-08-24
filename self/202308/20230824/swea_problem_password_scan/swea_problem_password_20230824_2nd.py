import sys
sys.stdin = open('input.txt')

transform = {(2, 1, 1):0, (2, 2, 1):1, (1, 2, 2):2, (4, 1, 1):3, (1, 3, 2):4, (2, 3, 1):5, (1, 1, 4):6, (3, 1, 2):7, (2, 1, 3):8, (1, 1, 2):9}
# 암호 해독에 쓰일 딕셔너리 정의
Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    raw_data = sorted(list(set([input().strip() for _ in range(N)]))) # 값을 받아오면서 set에 저장함으로서 중복된 값을 제거
    raw_data.pop(0) # 정렬된 상태이므로 젤 앞의 값은 0으로 이루어진 값
    # print(raw_data)
    raw_password = '' # 암호 데이터를 합칠 변수
    for data in raw_data: # 받아온 암호 코드를 순회하면서
        data = data.rstrip('0') # 뒤의 '0'을 제거하고
        # print(data)
        raw_password += data # 암호 데이터를 합침
    raw_binary_data = bin(int(raw_password, base=16)) # 16진수 상태인 암호 데이터를 2진수로 변경
    raw_binary_data = raw_binary_data.rstrip('0') # 끝에 붙어있는 0을 모두 제거
    raw_binary_data = raw_binary_data[2:] # 앞에 붙어있는 '0b'를 제거
    raw_binary_data = '0' + raw_binary_data # 맨 앞에 0을 붙여줌(아래 코드 때문에 필요함)
    # print(raw_binary_data)

    check_list = [] # 변환된 데이터인지 체크할 리스트를 선언
    ans = 0 # 해독된 암호들의 합을 저장할 변수 선언

    code = [] # 해독된 코드를 넣을 리스트 선언
    length = len(raw_binary_data) # 해독할 암호 길이 측정
    n1 = n2 = n3 = n4 = 0 # 1과 0의 비율을 측정하기 위해 필요한 변수 선언
    for idx in range(length - 1, -1, -1): # 해독이 필요한 암호를 뒤에서부터 읽어나가면서
        if raw_binary_data[idx] == '1' and not n3: # 1을 만나면 (뒤의 0을 잘라줬기 때문에 맨 마지막 값은 항상 0)
            n4 += 1
        elif raw_binary_data[idx] == '0' and not n2: # 0을 만나면
            n3 += 1
        elif raw_binary_data[idx] == '1' and not n1: # 1을 만나면
            n2 += 1
        elif raw_binary_data[idx] == '0': # 맨 앞에 0을 붙여준 이유, 0을 만나면 암호를 해독할 준비를 함(2진수로 변경된 암호의 시작은 항상0, 끝은 항상1)
            if raw_binary_data[idx - 1] == '1': # 해당 인덱스의 앞에 1이 있다면 암호 해독을 시작
                n = min(n2, n3, n4) # 최소값을 구함, 해당 공정이 가능한 이유는 최소 크기의 암호 비율에 늘 1이 포함됨
                code.append(transform[n2 // n, n3 // n, n4 // n])
                n1 = n2 = n3 = n4 = 0
                if len(code) == 8:
                    if code not in check_list:
                        if not ((code[7] + code[5] + code[3] + code[1]) * 3 + code[6] + code[4] + code[2] + code[0]) % 10:
                            ans += sum(code)
                            # print(code)
                            check_list.append(code[:])
                    code = []

    print(f'#{test + 1} {ans}')
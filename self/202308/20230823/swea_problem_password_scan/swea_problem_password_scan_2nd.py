import sys
sys.stdin = open('input.txt')


bi_dict = {'0001101': '0',
           '0011001': '1',
           '0010011': '2',
           '0111101': '3',
           '0100011': '4',
           '0110001': '5',
           '0101111': '6',
           '0111011': '7',
           '0110111': '8',
           '0001011': '9'}

Test = int(input())
for test in range(14):
    N, M = map(int, input().split())
    raw_data = set()
    for _ in range(N):
        data = input()
        for char in data:
            if char != '0':
                break
        else:
            continue
        raw_data.add(data)
    # print(raw_data) # 출력용
    censored_data = []

    for data in raw_data:
        something = bin(int(data, base=16))
        censored_data.append('0'*37*3 + something[2:])

    data_list = []
    for data in censored_data:

        while '1' in data:
            while True: # 맨 뒤의 0을 잘라내는 과정
                length = len(data)
                if data[length-1] == '0':
                    data = data[:length-1]
                else:
                    break

            for i in range(1, 37):
                sample_data = data[-7*i:]
                test_data = ''
                for j in range(0, 7*i, i):
                    test_data += sample_data[j]
                if test_data in bi_dict:
                    break

            password_data = data[-56*i:]
            data = data[:len(data)-56*i+1]
            if len(password_data) == 56*i:
                data_list.append([password_data, i])

    print(data_list)


    password_set = set()
    for data, i in data_list:
        fake = False
        password = ''

        for k in range(0, 56 * i, i):
            password += data[k]

        if not fake:
            real_password = ''
            for j in range(8):
                if password[0+j*7:7+j*7] in bi_dict:
                    real_password += bi_dict[password[0+j*7:7+j*7]]
            if len(real_password) == 8:
                password_set.add(real_password)
    print(password_set)
    #답을 산출하는 과정
    sum_val = 0
    for password in password_set:
        check_val = 0
        for idx in range(8):
            if idx % 2:
                check_val += int(password[idx])
            else:
                check_val += int(password[idx])*3
        if not check_val % 10:
            for char in password:
                sum_val += int(char)
    print(f'#{test+1} {sum_val}')


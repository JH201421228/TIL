import sys
sys.stdin = open('input.txt')


bi_dict = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
transform = {(2, 1, 1):0, (2, 2, 1):1, (1, 2, 2):2, (4, 1, 1):3, (1, 3, 2):4, (2, 3, 1):5, (1, 1, 4):6, (3, 1, 2):7, (2, 1, 3):8, (1, 1, 2):9}
Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    # raw_data = sorted(list(set([input() for _ in range(N)])))
    raw_data = sorted(list(set([input().strip() for _ in range(N)])), reverse=True)
    raw_data.pop()
    # print(raw_data)

    raw_password = ''
    for i in range(len(raw_data)):
        raw_data[i] = raw_data[i].rstrip('0')
        for j in range(len(raw_data[i])):
            raw_password += raw_data[i][j]
    raw_password = bin(int(raw_password, base=16))
    raw_password = raw_password.rstrip('0')
    # print(raw_password)
    check_list = []
    ans = 0

    code = []
    length = len(raw_password)
    n1 = n2 = n3 = n4 = 0
    for idx in range(length-1, -1, -1):
        if raw_password[idx] == '1' and not n3:
            n4 += 1
        elif raw_password[idx] == '0' and not n2:
            n3 += 1
        elif raw_password[idx] == '1' and not n1:
            n2 += 1
        elif raw_password[idx] == '0':
            if raw_password[idx-1] == '1':
                n = min(n2, n3, n4)
                code.append(transform[n2//n, n3//n, n4//n])
                n1 = n2 = n3 = n4 = 0
                if len(code) == 8:
                    if code not in check_list:
                        if not ((code[7] + code[5] + code[3] + code[1]) * 3 + code[6] + code[4] + code[2] + code[0]) % 10:
                            ans += sum(code)
                            check_list.append(code[:])
                    code = []

    print(f'#{test+1} {ans}')
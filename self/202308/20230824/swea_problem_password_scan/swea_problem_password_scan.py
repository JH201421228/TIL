import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    maybe_password = set()
    for i in range(N):
        check_plz_list = input()
        for char in check_plz_list.split('0'):
            if char:
                maybe_password.add(char)
    print(maybe_password)
    password_list = []
    for password in maybe_password:
        password_list.append(bin(int(password, base=16)))
    print(password_list)
    for inner in password_list:
        cnt = 0
        idx = -1
        while inner[idx] == '0':
            cnt += 1
            idx -= 1
        print(len(inner) - 2 - cnt)
    # for password in password_list:
    #     password[2:9]
    #     password[9:]


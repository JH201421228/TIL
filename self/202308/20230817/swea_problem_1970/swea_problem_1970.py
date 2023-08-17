import sys
sys.stdin = open('input.txt')

Test = int(input())
for test in range(Test):
    money = int(input())
    current = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans_dict = {}
    for i in range(8):
        ans_dict[current[i]] = ans_dict.get(current[i], money//current[i])
        money %= current[i]
    print(f'#{test + 1}')
    for val in ans_dict.values():
        print(val, end=' ')
    print()

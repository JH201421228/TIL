import sys
sys.stdin = open('input2.txt')

Test = int(input())
for test in range(Test):
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
    print(raw_data)
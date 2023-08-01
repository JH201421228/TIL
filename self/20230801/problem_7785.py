import sys
input = sys.stdin.readline

Test_Case = int(input())
status_dict = {}
status_list = []

for test_case in range(Test_Case):
    key, value = map(str, input().split())
    status_dict[key] = value

for name, status in status_dict.items():
    if status == 'enter':
        status_list.append(name)

status_list.sort(reverse= True)

for name in status_list:
    print(name)
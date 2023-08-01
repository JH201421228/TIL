import sys
input = sys.stdin.readline

No_hear, No_see = map(int, input().split())
name_dict = {}
for i in range(No_hear + No_see):
    name = input().rstrip()
    name_dict[name] = name_dict.get(name, 0) + 1

ans_list = []
num = 0
for key, value in name_dict.items():
    if value == 2:
        ans_list.append(key)
        num += 1

ans_list.sort()
print(num)
for name in ans_list:
    print(name)
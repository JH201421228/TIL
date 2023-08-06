import sys
sys.stdin = open('input.txt')

num_of_people = int(input())
people_list = list(map(int, input().split()))
people_stack = []
people_num = 1
people_length = len(people_list)

while people_list:
    if people_list and people_list[0] == people_num:
        del people_list[0]
        people_num += 1
    elif people_stack and people_stack[-1] == people_num:
        people_stack.pop()
        people_num += 1
    else:
        people_stack.append(people_list[0])
        del people_list[0]

for _ in range(len(people_stack)):
    num = people_stack.pop()
    if num != people_num:
        print('Sad')
        break
    else:
        people_num += 1

if people_num == people_length + 1:
    print('Nice')
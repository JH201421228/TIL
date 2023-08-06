import sys
sys.stdin = open('input.txt')

num_of_people = int(input())
people_list = list(map(int, input().split()))
people_stack = []
people_num = 1
while True:
    if people_list and people_list[0] == people_num:
        del people_list[0]
        people_num += 1

    elif people_stack and people_stack[-1] == people_num:
        people_stack.pop()
        people_num += 1

    elif (people_list and people_list[0] != people_num) and (people_stack and people_stack[-1] != people_num):
        print('sad')
        break

    elif not people_list and (people_stack and people_stack[-1] != people_num):
        print('sad')
        break

    elif (people_list and people_list[0] != people_num) and not people_stack:
        print('sad')
        break

    if not people_list and not people_stack:
        print('nice')
        break
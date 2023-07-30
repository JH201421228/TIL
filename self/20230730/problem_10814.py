N = int(input())

ans_list = []

for i in range(N):
    input_data = str(input())
    age_name = input_data.split(' ')
    age_num_name = [int(age_name[0]), i, age_name[1]]
    ans_list.append(age_num_name)

ans_list.sort()

for i, j, k in ans_list:
    print(i, k)
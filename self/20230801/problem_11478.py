input_str = input()

ans_set = set()

for i in range(len(input_str)):
    for j in range(len(input_str)-i):
        ans_set.add(input_str[j:j+(i+1)])

print(len(ans_set))
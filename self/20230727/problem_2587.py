integer_list = []

for i in range(5):
    integer_list.append(int(input()))

nums_average = sum(integer_list) / 5

integer_list.sort()

nums_median = integer_list[2]

print(int(nums_average))
print(nums_median)
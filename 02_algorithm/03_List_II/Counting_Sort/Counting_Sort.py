import sys
sys.stdin = open('input.txt')

data = list(map(int, input().split()))
max_num = 4
counts = [0]*(max_num+1)
sorted_list = [0]*len(data)

for num in data:
    counts[num] += 1

for index in range(len(counts)-1):
    counts[index+1] += counts[index]

for num in data:
    counts[num] -= 1
    sorted_list[counts[num]] = num


print(data)
print(counts)
print(sorted_list)

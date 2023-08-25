import sys
sys.stdin = open('input.txt')


total_j, total_i = map(int, input().split())
start_j, start_i = map(int, input().split())
time = int(input())

end_i = start_i + time
end_j = start_j + time
i_x = end_i // total_i
j_x = end_j // total_j
# print(j_x, i_x)
if j_x % 2:
    ans_j = total_j - end_j % total_j
else:
    ans_j = end_j % total_j

if i_x % 2:
    ans_i = total_i - end_i % total_i
else:
    ans_i = end_i % total_i
print(ans_j, ans_i)



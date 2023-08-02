import sys
input = sys.stdin.readline

num_of_tree = int(input())
now_tree = []



# for _ in range(num_of_tree):
#     now_tree.append(int(input().rstrip()))

# start_cordinate = now_tree[0]
# end_cordinate = now_tree[-1]

# between_tree = []
# for i in range(len(now_tree)-1):
#     between_tree.append(now_tree[i+1]-now_tree[i])

# short_length_between_tree = min(between_tree)

# ideal_tree = []

# for i in range(start_cordinate, end_cordinate+1, short_length_between_tree):
#     ideal_tree.append(i)

# print(len(set(ideal_tree)-set(now_tree)))
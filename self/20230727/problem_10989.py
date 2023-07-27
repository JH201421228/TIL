N = int(input())
problem_list = []

for _ in range(N):
    problem_list.append(int(input()))

problem_list.sort()

for i in problem_list:
    print(i)
import sys
sys.stdin = open('input.txt')

N = int(input())
change = list(map(int, input().split()))
students = list(i+1 for i in range(N))
for i in range(N):
    popped_student = students.pop(i)
    students.insert(i - change[i], popped_student)
print(*students)
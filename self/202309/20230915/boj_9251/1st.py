import sys
sys.stdin = open('input.txt')

string1 = list(input())
string2 = list(input())
length1 = len(string1) + 1
length2 = len(string2) + 1

matrix = [[0]*length1 for _ in range(length2)]
for i in range(1, length2):
    for j in range(1, length1):
        if string1[j-1] == string2[i-1]:
            matrix[i][j] = matrix[i-1][j-1] + 1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
print(matrix[-1][-1])
# print(matrix)
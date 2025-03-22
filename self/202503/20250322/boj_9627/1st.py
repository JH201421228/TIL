import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N = int(input())

S = [input().rstrip() for _ in range(N)]

length = 0
index = 0
for idx in range(N):
    if S[idx] != '$':
        length += len(S[idx])
    else:
        index = idx

integer_string = [''] * 1000
integer_length = [0] * 1000

integer_string[1], integer_string[2], integer_string[3], integer_string[4], integer_string[5], integer_string[6], integer_string[7], integer_string[8], integer_string[9], integer_string[10] = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
integer_string[11], integer_string[12], integer_string[13], integer_string[14], integer_string[15], integer_string[16], integer_string[17], integer_string[18], integer_string[19] = "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
integer_string[20], integer_string[30], integer_string[40], integer_string[50], integer_string[60], integer_string[70], integer_string[80], integer_string[90] = "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
integer_string[100], integer_string[200], integer_string[300], integer_string[400], integer_string[500], integer_string[600], integer_string[700], integer_string[800], integer_string[900] = "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred", "sixhundred", "sevenhundred", "eighthundred", "ninehundred"

for i in range(2, 10):
    for j in range(1, 10):
        idx = i*10+j
        integer_string[idx] = integer_string[i*10] + integer_string[j]

for i in range(1, 10):
    for j in range(1, 100):
        idx = i*100+j
        integer_string[idx] = integer_string[i*100] + integer_string[j]

for i in range(1, 1000): integer_length[i] = len(integer_string[i])

for idx in range(1, 1000):
    if length + integer_length[idx] == idx:
        S[index] = integer_string[idx]
        break

print(*S)
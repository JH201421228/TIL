import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def moo_length(N):
    s = [3]
    i = 1
    while s[-1] < N:
        s.append(s[i-1] * 2 + (i+3))
        i += 1
    return s, i

def find_Nth_char(N, i):

    while N > 3:
        if N <= s[i-2]:
            pass
        elif N > s[i-2] + (i+2):
            N -= s[i-2] + (i+2)
        else:
            return 'm' if N - s[i-2] == 1 else 'o'
        i -= 1

    return 'm' if N == 1 else 'o'

N = int(input())
s, i = moo_length(N)
# print(s, i)
print(find_Nth_char(N, i))
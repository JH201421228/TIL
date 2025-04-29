import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, M = map(int, input().split())

cases = [0]
cases.append(N)
cases.append(N//2)
cases.append((N+1)//2)
cases.append((N+2)//3)
cases.append(cases[1] + cases[4])
cases.append(cases[2] + cases[4])
cases.append(cases[3] + cases[4])

if N == 1:
    if M: print(2)
    else: print(1)
elif N == 2:
    if M > 1: print(4)
    elif M > 0: print(3)
    else: print(1)
else:
    ans = 0
    for n in cases:
        if n <= M: ans += 1

    print(ans)

print(cases)

# 0 0
# 1 N
# 2 N//2 + N%2
# 3 N//2 + N%2
# 4 (N+2)//3 + if((N+2)%3) + 1
# 1 4
# 2 4
# 3 4
#
# case 3 > 0
# else
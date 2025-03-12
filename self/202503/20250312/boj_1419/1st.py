import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def count(lcm, K, C, start, U):
    global cnt, lcm_list
    ea = (U - start) // lcm
    remain = U - (ea * lcm + start)
    remain_n = 0

    for idx in range(1, remain+1):
        if lcm_list[idx]:
            remain_n += 1

    print(remain, remain_n)

    return cnt * ea + 1 + remain_n

L = int(input())
R = int(input())
K = int(input())

constant = [0] * K
for idx in range(1, K):
    constant[idx] = constant[idx-1] + idx

start = K + constant[-1]
ans_r, ans_l = 0, 0

lcm_n = lcm(max(K, constant[-1]), min(K, constant[-1]))
lcm_list = [0] * (lcm_n+1)

for idx in range(K, lcm_n+1, K):
    lcm_list[idx] = 1

for idx in range(1, lcm_n+1):
    if lcm_list[idx] and idx + constant[-1] < lcm_n+1:
        lcm_list[idx+constant[-1]] = 1

    if not idx % constant[-1]:
        lcm_list[idx] = 1

cnt = 0
for idx in range(1, lcm_n+1):
    if lcm_list[idx]:
        cnt += 1

print(cnt)

if start <= R:
    ans_r = count(lcm_n, K, constant[-1], start, R)
    if L >= start:
        ans_l = count(lcm(max(K, constant[-1]), min(K, constant[-1])), K, constant[-1], start, L)
        print(ans_r, ans_l)
        print(ans_r - ans_l)
    else:
        print(ans_r)

else:
    print(0)
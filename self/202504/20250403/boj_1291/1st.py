def digit(n):
    # 자릿수 계산
    a = 0
    while True:
        b = n // (10 ** a)
        if b < 10:
            break
        a += 1
    return a + 1

def is_prime(n):
    if n == 1:
        return False
    a = 2
    while True:
        if n % a == 0:
            break
        a += 1
    return n == a

def check이면수(n):
    temp = n
    a = digit(n)
    v = []
    while a > 1:
        i = n // (10 ** (a - 1))
        v.append(i)
        n = n - (i * (10 ** (a - 1)))
        a -= 1
    v.append(n)
    b = sum(v)
    if temp >= 4 and temp != 5 and b % 2 == 1:
        return True
    else:
        return False

def check임현수(n):
    v = []
    if n == 2 or n == 4:
        return True
    elif is_prime(n) or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0 and is_prime(i):
                v.append(i)
        return len(set(v)) % 2 == 0

def classify_number(n):
    is_yeemyeon = check이면수(n)
    is_imhyeon = check임현수(n)

    if is_yeemyeon and is_imhyeon:
        return 4
    elif is_yeemyeon:
        return 1
    elif is_imhyeon:
        return 2
    else:
        return 3

# 입력 처리
N = int(input())
print(classify_number(N))

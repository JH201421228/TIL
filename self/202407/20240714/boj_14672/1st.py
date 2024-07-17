import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def isPrime(n):
    for i in range(2, int(n**0.5+1)):
        if prime[i] and not n%i:
            return False

    return True


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


N, M = map(int, input().split())
potions = [0] + list(map(int, input().split()))

prime = [1] * int(N**0.5+1)
prime_dict = dict()
cnt = 0
for i in range(2, int(N**0.5+1)):
    if prime[i]:
        prime_dict[i] = cnt = cnt +1
        for j in range(i**2, int(N**0.5+1), i):
            prime[j] = 0

G = [[] for _ in range(M+1)]
for i in range(1, M+1):
    if isPrime(potions[i]):
        if potions[i] in prime_dict:
            G[i].append(prime_dict[potions[i]])
        else:
            prime_dict[potions[i]] = cnt = cnt+1
            G[i].append(cnt)
    else:
        for j in range(2, int(potions[i]**0.5+1)):
            if prime[j] and not potions[i]%j:
                G[i].append(prime_dict[j])
                if isPrime(potions[i]//j):
                    if potions[i]//j in prime_dict:
                        G[i].append(prime_dict[potions[i]//j])
                    else:
                        prime_dict[potions[i]//j] = cnt = cnt+1
                        G[i].append(cnt)

C = [0]*(cnt+1)
ans = 0
for i in range(1, M+1):
    V = [0]*(cnt+1)
    if B(i):
        ans += 1

print(ans)
print(prime_dict)
print(G)
print(prime)
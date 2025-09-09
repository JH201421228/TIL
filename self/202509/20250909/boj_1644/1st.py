import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = 4_000_000
isPrime = [1] * n
primes = []


def sieve():
    isPrime[0] = 0
    isPrime[1] = 0

    for i in range(2, int(n**.5)+1):
        if isPrime[i]:
            for j in range(i**2, n, i):
                isPrime[j] = 0

    for i in range(n):
        if isPrime[i]: primes.append(i)

    return


def solve(N):

    s, e = 0, 1
    length = len(primes)
    cur = primes[0]
    ans = 0
    while True:
        if cur == N:
            ans += 1
            if e == length: break
            cur += primes[e]
            e += 1

        elif cur < N:
            if e == length: break

            cur += primes[e]
            e += 1

        else:
            cur -= primes[s]
            s += 1

            if s == e and e == length: break


    print(ans)

    return


def main():

    sieve()

    solve(int(input()))

    return


if __name__ == "__main__":
    main()
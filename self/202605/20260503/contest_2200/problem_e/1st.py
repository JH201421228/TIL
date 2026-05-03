import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]: return False
    
    return True


def solve(perfect):
    N = int(input())
    arr = list(map(int, input().split()))
    
    if is_sorted(arr):
        print("Bob")
        return
    
    for i in range(N):
        if not perfect[arr[i]]:
            print("Alice")
            return
        arr[i] = perfect[arr[i]]
    
    if is_sorted(arr): print("Bob")
    else: print("Alice")
    
    return


def main():
    sieve = [1] * 1_000_001
    for i in range(2, 1_001):
        for j in range(2*i, 1_000_001, i): sieve[j] = 0
    
    perfect = [0] * 1_000_001
    perfect[1] = 1
    
    for i in range(2, 1_000_001):
        if not sieve[i]: continue
        
        cur = i
        
        while cur < 1_000_001:
            perfect[cur] = i
            cur *= i
    
    for _ in range(int(input())): solve(perfect)
    
    return


if __name__ == "__main__":
    main()
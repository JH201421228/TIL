import sys, random
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    s = int(random.uniform(0, 1) * 10_000)
    
    idx = 0
    while True:
        print(f"? A {(s + idx) % 10_000 + 1}", flush=True)
        
        if int(input()):
            break
        
        idx += 1
        
    A = (s + idx) % 10_000 + 1
    
    idx = 0
    while True:
        print(f"? B {(s + idx) % 10_000 + 1}", flush=True)
        
        if int(input()):
            break
        
        idx += 1
        
    print("!", A + (s + idx) % 10_000 + 1)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
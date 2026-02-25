import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def cleansing(N):
    times = []
    
    for _ in range(N):
        temp = tuple(input().rstrip().split(" - "))
        time = []
        
        for t in temp:
            t = tuple(map(int, t.split(":")))
            time.append(3600 * t[0] + 60 * t[1] + t[2])
        
        times.append(time)
    
    return times


def solve():
    N = int(input())
    
    times = cleansing(N)
    
    table = [0] * (3600*24+1)
        
    for time in times:
        s, e = time
        if s <= e:
            table[s] += 1
            table[e+1] -= 1
        else:
            table[0] += 1
            table[e+1] -= 1
            table[s] += 1
            table[3600*24] -= 1
        
        
    for t in range(1, 3600*24+1):
        table[t] += table[t-1]
    
    for t in range(1, 3600*24+1):
        table[t] += table[t-1]
        
    query = cleansing(int(input()))
    
    for q in query:
        s, e = q
        
        if s <= e:
            total = table[e] - (table[s-1] if s > 0 else 0)
            length = e-s+1
            print(total / length)
        else:
            left = table[3600*24-1] - (table[s-1] if s > 0 else 0)
            right = table[e]
            length = 3600*24 - s + e + 1
            print((left+right) / length)
            
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
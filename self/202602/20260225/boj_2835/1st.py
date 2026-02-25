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
        
        if time[1] < time[0]: time[1] += 3600*24
        
        times.append(time)
    
    return times


def solve():
    N = int(input())
    
    times = cleansing(N)
    
    table = [0] * (3600*24*2+2)
        
    for time in times:
        table[time[0]+1] += 1
        table[time[1]+2] -= 1
        
    for idx in range(1, 3600*24*2+2):
        table[idx] += table[idx-1]
    
    for idx in range(1, 3600*24*2+2):
        table[idx] += table[idx-1]
        
    for idx in range(3600*24+1, 3600*24*2+2):
        table[idx] += table[idx-3600*24]
        
    query = cleansing(int(input()))
    
    for q in query:
        print((table[q[1]+1] - table[q[0]]) / (q[1]-q[0]+1))

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
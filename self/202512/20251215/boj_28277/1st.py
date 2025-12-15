import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    N, Q = map(int, input().split())
    
    sets = []
    ans = []
    
    for _ in range(N):
        temp = tuple(map(int, input().split()))
        sets.append(set(temp[1:]))

    
    for _ in range(Q):
        temp = tuple(map(int, input().split()))
        
        if temp[0] == 2:
            ans.append(str(len(sets[temp[1]-1])))
            
        else:
            if len(sets[temp[1]-1]) <= len(sets[temp[2]-1]):
                sets[temp[1]-1], sets[temp[2]-1] = sets[temp[2]-1], sets[temp[1]-1]
                
            sets[temp[1]-1].update(sets[temp[2]-1])
            sets[temp[2]-1].clear()
    
    print('\n'.join(ans))
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
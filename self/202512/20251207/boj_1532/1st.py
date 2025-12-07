import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    state = list(map(int, input().split()))
    temp = list(map(int, input().split()))
    
    for idx in range(3):
        state[idx] -= temp[idx]
        
    ans = 0
        
    while True:
        
        if state[0] >= 0 and state[1] >= 0 and state[2] >= 0:
            print(ans)
            break
        
        if state[0] <= 0 and state[1] <= 0 and state[2] <= 0:
            print(-1)
            break
        
        if state[0] < 0:
            if state[1] >= 11:
                state[0] += 1
                state[1] -= 11
                ans += 1
            elif state[2] >= 11:
                state[1] += 1
                state[2] -= 11
                ans += 1
            else:
                print(-1)
                break
        elif state[1] < 0:
            if state[0] > 0:
                state[0] -= 1
                state[1] += 9
                ans += 1
            elif state[2] >= 11:
                state[1] += 1
                state[2] -= 11
                ans += 1
            else:
                print(-1)
                break
        elif state[2] < 0:
            if state[1] > 0:
                state[1] -= 1
                state[2] += 9
                ans += 1
            elif state[0] > 0:
                state[0] -= 1
                state[1] += 9
                ans += 1
            else:
                print(-1)
                break
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
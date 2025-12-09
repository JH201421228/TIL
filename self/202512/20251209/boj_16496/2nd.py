import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline



def solve():
    N = int(input())
    temp = list(map(int, input().split()))
    
    S1, S2 = [], []
    
    for t in temp:
        if not S1:
            S1.append(t)
        else:
            if int(str(S1[-1]) + str(t)) >= int(str(t) + str(S1[-1])):
                if not S2:
                    S2.append(t)
                else:
                    if int(str(t) + str(S2[-1])) < int(str(S2[-1]) + str(t)):
                        while S2 and int(str(t) + str(S2[-1])) < int(str(S2[-1]) + str(t)):
                            S1.append(S2.pop())
                    S2.append(t)
            else:
                while S1 and int(str(S1[-1]) + str(t)) < int(str(t) + str(S1[-1])):
                    S2.append(S1.pop())
                S1.append(t)
                
    ans = ''.join(list(map(str, S1)))
    while S2:
        ans += str(S2.pop())
        
    if ans[0] == '0': print(0)
    else: print(ans)

    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
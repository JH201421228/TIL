import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def solve():
    x, y = map(int, input().split())
    command = input().rstrip()
    
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    cur_x, cur_y = 0, 0
    
    ans = (0, 0)
    dist = (x**2 + y**2)
    
    com = command[0]
    idx = 1
    n = ""
    
    while idx < len(command):
        n += command[idx]
        idx += 1
        
        if idx == len(command) or command[idx] in ["S", "T"]:
            
            if com == "S":
                prev_x, prev_y = cur_x, cur_y
                cur_x, cur_y = cur_x + delta[d][0] * int(n), cur_y + delta[d][1] * int(n)
                
                if x >= min(prev_x, cur_x) and x <= max(prev_x, cur_x):
                    if dist > (cur_y - y)**2:
                        dist = (cur_y - y)**2
                        ans = (x, cur_y)
                        
                if y >= min(prev_y, cur_y) and y <= max(prev_y, cur_y):
                    if dist > (cur_x - x)**2:
                        dist = (cur_x - x)**2
                        ans = (cur_x, y)
                        
                if dist > ((x-prev_x)**2 + (y-prev_y)**2):
                    dist = ((x-prev_x)**2 + (y-prev_y)**2)
                    ans = (prev_x, prev_y)
                    
                if dist > ((x-cur_x)**2 + (y-cur_y)**2):
                    dist = ((x-cur_x)**2 + (y-cur_y)**2)
                    ans = (cur_x, cur_y)
                
            else:
                d += int(n)
                d %= 4
                
            if idx == len(command): break
            
            com = command[idx]
            idx += 1
            n = ""
    
    
    if ans == (x, y): print(-1)
    else: print(*ans)
    
    return


def main():
    solve()
    
    return


if __name__ == "__main__":
    main()
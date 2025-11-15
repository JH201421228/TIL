import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


ans = []

def is_same_dot(lines):
    global ans
    
    def _temp(dot1, dot2):
        if dot1 == dot2:
            return True

        return False
    
    if _temp(lines[0][:2], lines[1][:2]):
        if lines[0][:2] not in ans: 
            ans.append(lines[0][:2])

    if _temp(lines[0][:2], lines[1][2:]):
        if lines[0][:2] not in ans:
            ans.append(lines[0][:2])

    if _temp(lines[0][2:], lines[1][:2]):
        if lines[0][2:] not in ans:
            ans.append(lines[0][2:])
    
    if _temp(lines[0][2:], lines[1][2:]):
        if lines[0][2:] not in ans:
            ans.append(lines[0][2:])
    
    return


def is_online(lines):
    global ans
    
    def _temp(d1, d2, d3):
        if (d3[0] >= min(d1[0], d2[0]) 
            and d3[0] <= max(d1[0], d2[0])
            and d3[1] >= min(d1[1], d2[1])
            and d3[1] <= max(d1[1], d2[1])):
            if (d1[1]-d3[1]) * (d2[0]-d3[0]) == (d2[1]-d3[1]) * (d1[0]-d3[0]):
                return True
            
        return False
    
    if _temp(lines[0][:2], lines[0][2:], lines[1][:2]):
        if lines[1][:2] not in ans:
            ans.append(lines[1][:2])
    
    if _temp(lines[0][:2], lines[0][2:], lines[1][2:]):
        if lines[1][2:] not in ans:
            ans.append(lines[1][2:])
    
    if _temp(lines[1][:2], lines[1][2:], lines[0][:2]):
        if lines[0][:2] not in ans:
            ans.append(lines[0][:2])
    
    if _temp(lines[1][:2], lines[1][2:], lines[0][2:]):
        if lines[0][2:] not in ans:
            ans.append(lines[0][2:])

    return


def ccw(lines):
    d1 = lines[0][:2]
    d2 = lines[0][2:]
    d3 = lines[1][:2]
    d4 = lines[1][2:]

    
    if (((d3[0]-d2[0]) * (d2[1]-d1[1]) - (d2[0]-d1[0]) * (d3[1]-d2[1]))
        * ((d4[0]-d2[0]) * (d2[1]-d1[1]) - (d2[0]-d1[0]) * (d4[1]-d2[1])) < 0):
        
        if (((d1[0]-d3[0]) * (d3[1]-d4[1]) - (d3[0]-d4[0]) * (d1[1]-d3[1]))
            * ((d2[0]-d3[0]) * (d3[1]-d4[1]) - (d3[0]-d4[0]) * (d2[1]-d3[1])) < 0):
            
            if d2[0] == d1[0]:
                x = d1[0]
                y = ((d4[1]-d3[1]) * (x-d3[0])) / (d4[0]-d3[0]) + d3[1]
                
                print(1)
                print(x, y)
                return
                
            if d4[0] == d3[0]:
                x = d3[0]
                y = ((d2[1]-d1[1]) * (x-d1[0])) / (d2[0]-d1[0]) + d1[1]
                
                print(1)
                print(x, y)
                return
            
            print(1)
            
            alpha1 = (d2[1]-d1[1]) / (d2[0]-d1[0])
            alpha2 = (d4[1]-d3[1]) / (d4[0]-d3[0])
            
            x = (alpha1*d1[0] - alpha2*d3[0] - d1[1] + d3[1]) / (alpha1 - alpha2)
            y = alpha1 * (x - d1[0]) + d1[1]
            
            print(x, y)
            
            return

    print(0)
    
    return


def cross_check(lines):
    global ans
    
    is_same_dot(lines)
    is_online(lines)
    
    if len(ans) > 1:
        print(1)
        return
    elif len(ans) == 1:
        print(1)
        print(*ans[0])
        return

    ccw(lines)

    return


def solve():
    lines = [tuple(map(int, input().split())) for _ in range(2)]
    
    cross_check(lines)

    return


def main():
    solve()

    return


if __name__ == "__main__":
    main()
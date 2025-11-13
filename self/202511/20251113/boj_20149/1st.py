import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


def is_same_dot(lines):
    def _temp(dot1, dot2):
        if dot1 == dot2:
            print(1)
            print(*dot1)
            return True

        return False
    
    if _temp(lines[0][:2], lines[1][:2]):
        return True

    if _temp(lines[0][:2], lines[1][2:]):
        return True

    if _temp(lines[0][2:], lines[1][:2]):
        return True
    
    if _temp(lines[0][2:], lines[1][2:]):
        return True
    
    return False


def is_online(lines):
    def _temp(d1, d2, d3):
        if (d3[0] >= min(d1[0], d2[0]) 
            and d3[0] <= max(d1[0], d2[0])
            and d3[1] >= min(d1[1], d2[1])
            and d3[1] <= max(d1[1], d2[1])):
            if (d1[1]-d3[1]) * (d2[0]-d3[0]) == (d2[1]-d3[1]) * (d1[0]-d3[0]):
                print(1)
                print(*d3)
                return True
            
        return False
    
    if _temp(lines[0][:2], lines[0][2:], lines[1][:2]):
        return True
    
    if _temp(lines[0][:2], lines[0][2:], lines[1][2:]):
        return True
    
    if _temp(lines[1][:2], lines[1][2:], lines[0][:2]):
        return True
    
    if _temp(lines[1][:2], lines[1][2:], lines[0][2:]):
        return True

    return False





def cross_check(lines):
    if is_same_dot(lines): return

    if is_online(lines): return



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